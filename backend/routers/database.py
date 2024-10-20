from typing import Any, Annotated

from logger import get_logger

from fastapi import APIRouter, Query, Path, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from models import MatchModel, SummonerAndSpectorServerModel, MatchType
from schemas import CurrentGameInfo
from utils.wrappers import map_puuid_and_server, map_identity_to_puuid
from database.database import get_db
from routers_services.database.matches_num_in_dbs import (
    resolve_data_intergrity,
    get_summoner_id,
)
from database.models.match.match_participant import MatchParticipant

logger = get_logger(__name__)
router = APIRouter()


@router.get("/matches/{server}/{identity}")
@map_identity_to_puuid
async def get_matches(
    server: SummonerAndSpectorServerModel,
    identity: str,
    summoner_name: str = Query(None, include_in_schema=False),
    puuid: str = Query(None, include_in_schema=False),
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
    """Fetches data with last games requested summoner participated in"""

    # Resolves whether server data is up to date with Riot API
    await resolve_data_intergrity(
        server=server,
        mapped_server=mapped_server,
        puuid=puuid,
        match_type=match_type,
        db=db,
    )
    (summoner, _) = await get_summoner_id(server, db, puuid)
    matches = (
        db.execute(
            select(MatchParticipant)
            .filter(MatchParticipant.summoner_id == summoner.id)
            .limit(count)
        )
        .scalars()
        .all()
    )

    return matches


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
