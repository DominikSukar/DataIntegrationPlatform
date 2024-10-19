from logger import get_logger
from fastapi import Query
from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload

from models import SummonerAndSpectorServerModel, MatchType, MatchModel
from database.models.summoner import Summoner
from database.models.basic import Server
from database.models.match.match import Match
from database.models.match.match_participant import MatchParticipant
from routers.summoner import get_summoner as get_summoner_from_riot_api
from routers.account import get_account_info as get_account_name_from_riot_api
from utils.mappers import (
    convert_LeagueAndSummonerEntryDTO_to_Summoner as map_to_summoner_model,
)
from routers_services.database.matches_data import get_matches_data

logger = get_logger(__name__)


async def return_summoner_comparison(
    server: SummonerAndSpectorServerModel,
    db: Session,
    puuid: str = Query(None, include_in_schema=False),
):

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

    (summoner_from_db, summoner_from_api) = await return_summoner_comparison(
        server, db, puuid
    )

    riot_api_match_count = summoner_from_api.wins + summoner_from_api.losses
    if riot_api_match_count == 0:
        logger.debug(
            f"User's {puuid}: <({summoner_from_db.nickname = }), ({summoner_from_db.tag = })> DB data is integrated with Riot's DB "
        )
        return None

    matches_user_participated_in = db.execute(
        select(MatchParticipant).filter(MatchParticipant.id == summoner_from_db.id)
    ).fetchall()
    db_match_count = len(matches_user_participated_in)
    logger.debug(
        f"Matches summoner <{puuid}, {server}> participated in are: {riot_api_match_count = }, {db_match_count = }"
    )
    match_count_diff = riot_api_match_count - db_match_count

    if match_count_diff > 0:
        logger.debug(
            f"Data intergrity check: matches count for user {puuid} needs an update from Riot's API. The difference is {match_count_diff}"
        )

        raw_matches, mapped_matches = await get_matches_data(
            puuid,
            mapped_server,
            match_count=100,
            match_type=match_type,
            start_time=1727215200,
        )
        logger.debug(
            f"Fetched matches: {raw_matches}, mapped matches: {mapped_matches}"
        )
        for match in mapped_matches:
            new_match = Match(**match)
            db.add(new_match)
        # db.commit()

        for match in raw_matches:
            participant = match["info"]["participants"]  # noqa: F841
            # mapped_match_participant = await match_participants_mapper(participant)

        return mapped_matches

    elif match_count_diff == 0:
        logger.debug(
            f"Data intergrity check: matches count for user {puuid} is up to date. The values are {db_match_count = } and {riot_api_match_count = }"
        )

    else:
        logger.error(
            f"Data intergrity check: matches count for user {puuid} is higher in database. The difference is {db_match_count-riot_api_match_count}"
        )
