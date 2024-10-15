import logging

from fastapi import Query, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload

from models import SummonerAndSpectorServerModel
from database.models.summoner import Summoner
from database.models.basic import Server
from database.models.match.match_participant import MatchParticipant
from database.database import get_db
from routers.summoner import get_summoner as get_summoner_from_riot_api
from routers.account import get_account_info as get_account_name_from_riot_api
from utils.mappers import (
    convert_LeagueAndSummonerEntryDTO_to_Summoner as map_to_summoner_model,
)

logger = logging.getLogger(__name__)


async def get_matches_counts(
    server: SummonerAndSpectorServerModel,
    puuid: str = Query(None, include_in_schema=False),
    db: Session = Depends(get_db),
):
    """
    Function returns for provided puuid and server numbers that are matches for a user in the Riot DB and applications' DB.
    If requested puuid for the server is not registered in DB then it is created and returned.

    Idea is to be able to check whether DB is not behind the offcial Riot DB.
    """

    def get_summoner_from_db(puuid: str, server: str):
        return db.execute(
            select(Summoner)
            .options(joinedload(Summoner.server))
            .join(Server)
            .filter(Summoner.puuid == puuid)
            .filter(Server.symbol == server)
        ).scalar_one_or_none()

    summoner = get_summoner_from_db(puuid, server)
    summoner_from_api = await get_summoner_from_riot_api(puuid=puuid, server=server)

    if not summoner:
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

        # Fetch summoner from database in order to get assigned ID
        summoner = get_summoner_from_db(puuid, server)

        assert summoner

    matches_in_riot_api = summoner_from_api.wins + summoner_from_api.losses
    if matches_in_riot_api == 0:
        return []

    matches_played_by_summoner = db.execute(
        select(MatchParticipant).filter(MatchParticipant.id == summoner.id)
    ).fetchall()

    matches_stored_in_db = len(matches_played_by_summoner)

    logger.debug(
        f"Matches summoner <{puuid}, {server}> participated in are: {matches_in_riot_api = }, {matches_stored_in_db = }"
    )
    return (matches_in_riot_api, matches_stored_in_db)
