import logging
from typing import Any, Annotated

from fastapi import APIRouter, Query, Path, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload

from models import MatchModel, SummonerAndSpectorServerModel, MatchType
from schemas import CurrentGameInfo
from utils.wrappers import map_puuid_and_server
from database.models.summoner import Summoner
from database.models.basic import Server
from database.database import get_db
from routers.summoner import get_summoner as get_summoner_from_riot_api
from routers.account import get_account_info as get_account_name_from_riot_api
from utils.mappers import (
    convert_LeagueAndSummonerEntryDTO_to_Summoner as map_to_summoner_model,
)

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/matches/{server}/{puuid}")
@map_puuid_and_server
async def get_matches(
    server: SummonerAndSpectorServerModel,
    puuid: str,
    mapped_server: MatchModel = Query(None, include_in_schema=False),
    match_type: Annotated[
        MatchType,
        Query(
            title="Query string",
            description="""Filter the list of match ids by the type of match. This filter is mutually inclusive of the queue filter meaning any match ids returned must match both the queue and type filters.
        Default value is ranked, so not need to pass it. Do not use '--', it's FastAPI/enum bug.""",
        ),
    ] = MatchType.ranked,
    count: int = Query(
        10,
        ge=0,
        le=100,
        description="Number of match ids to return. Valid values: 0 to 100.",
    ),
    db: Session = Depends(get_db),
):
    """Fetches data with last games of the requested user's"""

    # Is summoner in DB?
    summoner = db.execute(
        select(Summoner)
        .options(joinedload(Summoner.server))
        .join(Server)
        .filter(Summoner.puuid == puuid)
        .filter(Server.symbol == server)
    ).scalar_one_or_none()
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

        summoner = new_summoner

    # Is user's total game count equal to DB data?
    matches_stored_in_db = summoner.matches_played
    matches_in_riot_api = summoner_from_api.wins + summoner_from_api.losses
    if not matches_stored_in_db == matches_in_riot_api:
        logger.debug(
            f"Matches count for user {puuid} needs update from Riot's API. The difference is {matches_in_riot_api-matches_stored_in_db}"
        )
    elif matches_stored_in_db == matches_in_riot_api:
        logger.debug(f"Matches count for user {puuid} is up to date")
    else:
        logger.error(
            f"Matches count for user {puuid} is higher in database. The difference is {matches_stored_in_db-matches_in_riot_api}"
        )

    return summoner


@router.post("/matches/{server}/{puuid}")
async def post_match(
    server: SummonerAndSpectorServerModel,
    match_ID: Annotated[str, Path(examples="EUW1_7091585440")],
) -> CurrentGameInfo:
    "Posts data about a specific match from a database"
    pass

    return "Not working"


@router.get("/matches/{server}/{puuid}/{match_id}")
@map_puuid_and_server
async def get_match(
    server: SummonerAndSpectorServerModel,
    mapped_server: Any = Query(None, include_in_schema=False),
    summoner_name: str = None,
    puuid: str = None,
) -> CurrentGameInfo:
    """Gets data about a specific match from a database.
    Takes into account the user that requested it."""
    pass

    return "Not working"
