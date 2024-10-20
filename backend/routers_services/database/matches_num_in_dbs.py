from logger import get_logger
from fastapi import Query
from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload

from schemas import SummonerAndSpectorServerModel, MatchType, MatchModel
from database.models.summoner import Summoner
from database.models.basic import Server, Champion, Item, Perk, SummonerSpell
from database.models.match.match_team import MatchTeam
from database.models.match.match import Match
from database.models.match.match_participant import (
    MatchParticipant,
    MatchParticipantSummonerSpell,
    MatchParticipantPerk,
)
from routers.summoner import get_summoner as get_summoner_from_riot_api
from routers.account import get_account_info as get_account_name_from_riot_api
from utils.mappers import (
    convert_LeagueAndSummonerEntryDTO_to_Summoner as map_to_summoner_model,
)
from routers_services.database.matches_data import get_matches_ids, get_matches_data
from api_requests.mappers.match import (
    matches_mapper,
    match_teams_mapper,
    match_participants_mapper,
    match_participant_perks_mapper,
    match_participant_summoner_spells_mapper,
)

logger = get_logger(__name__)


async def get_summoner_id(
    server: SummonerAndSpectorServerModel,
    db: Session,
    puuid: str = Query(None, include_in_schema=False),
):
    logger.debug(f"Requested summoner {server = }, {puuid}")
    summoner_from_api = await get_summoner_from_riot_api(puuid=puuid, server=server)

    summoner_from_db = db.execute(
        select(Summoner)
        .options(joinedload(Summoner.server))
        .join(Server)
        .filter(Summoner.puuid == puuid)
        .filter(Server.symbol == server)
    ).scalar_one_or_none()

    if not summoner_from_db:
        logger.info(f"Requested data for new user: {puuid}")
        account_from_api = await get_account_name_from_riot_api(
            puuid=puuid, server=server
        )
        summoner_name = account_from_api.gameName
        summoner_tag = account_from_api.tagLine
        logger.debug(
            f"Fetched data for user {puuid}: <({summoner_name = }), ({summoner_tag = })>"
        )

        server_from_db = db.execute(
            select(Server).filter(Server.symbol == server)
        ).scalar_one_or_none()

        summoner_data = map_to_summoner_model(
            summoner_from_api,
            nickname=summoner_name,
            tag=summoner_tag,
            server_id=server_from_db.id,
        )
        new_summoner = Summoner(**summoner_data)
        db.add(new_summoner)
        db.commit()
        db.refresh(new_summoner)

        summoner_from_db = new_summoner

    return (summoner_from_db, summoner_from_api)


async def resolve_data_intergrity(
    server: SummonerAndSpectorServerModel,
    mapped_server: MatchModel,
    db: Session,
    puuid: str = Query(None, include_in_schema=False),
    match_type: MatchType = MatchType.ranked,
):
    """
    Function returns for provided puuid and server numbers that are matches for a user in the Riot DB and applications' DB.
    If requested puuid for the server is not registered in DB then it is created and returned.

    Idea is to be able to check whether DB is not behind the offcial Riot DB.
    """

    (summoner_from_db, summoner_from_api) = await get_summoner_id(server, db, puuid)

    riot_api_match_count = summoner_from_api.wins + summoner_from_api.losses
    if riot_api_match_count == 0:
        logger.debug(
            f"User's {puuid}: <({summoner_from_db.nickname = }), ({summoner_from_db.tag = })> DB data is integrated with Riot's DB "
        )
        return None

    matches_user_participated_in = db.execute(
        select(MatchParticipant).filter(
            MatchParticipant.summoner_id == summoner_from_db.id
        )
    ).fetchall()
    db_match_count = len(matches_user_participated_in)
    logger.debug(
        f"Matches summoner <{puuid}, {server.value}> participated in are: {riot_api_match_count = }, {db_match_count = }"
    )
    match_count_diff = riot_api_match_count - db_match_count

    if match_count_diff > 0:
        logger.debug(
            f"Data intergrity check: matches count for user {puuid} needs an update from Riot's API. The difference is {match_count_diff}"
        )

        riot_api_match_ids = await get_matches_ids(
            puuid,
            mapped_server,
            match_count=100,
            match_type=match_type,
            start_time=1727215200,
        )
        db_match_ids = db.execute(select(Match.riot_match_id)).scalars().all()
        match_ids_missing = list(set(riot_api_match_ids) - set(db_match_ids))
        logger.debug(f"Match IDs missing in DB: {len(match_ids_missing)}")

        if not match_ids_missing:
            logger.info("No match IDs")

        raw_matches = await get_matches_data(mapped_server, match_ids_missing)

        for raw_match in raw_matches:
            logger.debug(f"{raw_matches = }")
            match = matches_mapper(raw_match, server_id=2, split_id=4)
            new_match = Match(**match)
            db.add(new_match)
            db.flush()
            raw_teams = raw_match["info"]["teams"]

            participants = raw_match["info"]["participants"]
            participants_puuids = raw_match["metadata"]["participants"]
            for i, participant in enumerate(participants):
                participant["puuid"] = participants_puuids[i]

            for raw_team in raw_teams:
                team = match_teams_mapper(
                    team=raw_team, match_info=raw_match["info"], match_id=new_match.id
                )
                new_team = MatchTeam(**team)
                db.add(new_team)
                db.flush()

                for participant in participants:
                    if not participant["teamId"] == new_team.team_id:
                        continue
                    db_champion_id = db.execute(
                        select(Champion.id).filter(
                            Champion.riot_id == participant["championId"]
                        )
                    ).scalar_one_or_none()
                    items_ids = [
                        participant["item0"],
                        participant["item1"],
                        participant["item2"],
                        participant["item3"],
                        participant["item4"],
                        participant["item5"],
                        participant["item6"],
                    ]
                    db_items_ids = []
                    for item_id in items_ids:
                        db_item_id = db.execute(
                            select(Item.id).filter(Item.riot_id == item_id)
                        ).scalar_one_or_none()

                        db_items_ids.append(db_item_id)
                    (summoner_from_db, summoner_from_api) = await get_summoner_id(
                        server, db, participant["puuid"]
                    )
                    mapped_participant = match_participants_mapper(
                        participant,
                        summoner_id=summoner_from_db.id,
                        match_id=new_match.id,
                        match_team_id=new_team.id,
                        champion_id=db_champion_id,
                        items=db_items_ids,
                    )
                    new_participant = MatchParticipant(**mapped_participant)
                    db.add(new_participant)
                    db.flush()

                    mapped_match_participants_perks = match_participant_perks_mapper(
                        perks=participant["perks"],
                        match_participant_id=new_participant.id,
                    )
                    for perk in mapped_match_participants_perks:
                        db_perk_id = db.execute(
                            select(Perk.id).filter(Perk.riot_id == perk["perk_id"])
                        ).scalar_one_or_none()
                        perk["perk_id"] = db_perk_id
                        new_participant_perk = MatchParticipantPerk(**perk)
                        db.add(new_participant_perk)

                    summoner_spells = [
                        {"slot": 1, "summoner_spell_id": participant["summoner1Id"]},
                        {"slot": 0, "summoner_spell_id": participant["summoner2Id"]},
                    ]

                    for spell in summoner_spells:
                        db_summoner_spell_id = db.execute(
                            select(SummonerSpell.id).filter(
                                SummonerSpell.riot_id == spell["summoner_spell_id"]
                            )
                        ).scalar_one_or_none()
                        spell["summoner_spell_id"] = db_summoner_spell_id
                        mapped_spell = match_participant_summoner_spells_mapper(
                            slot=spell["slot"],
                            match_participant_id=new_participant.id,
                            summoner_spell_id=spell["summoner_spell_id"],
                        )
                        db.add(MatchParticipantSummonerSpell(**mapped_spell))

        db.commit()

        return None

    elif match_count_diff == 0:
        logger.debug(
            f"Data intergrity check: matches count for user {puuid} is up to date. The values are {db_match_count = } and {riot_api_match_count = }"
        )

    else:
        logger.error(
            f"Data intergrity check: matches count for user {puuid} is higher in database. The difference is {db_match_count-riot_api_match_count}"
        )
