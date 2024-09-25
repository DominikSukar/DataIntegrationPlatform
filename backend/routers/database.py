import logging
from typing import Any, Annotated

from fastapi import APIRouter, Query, Path
from models import SummonerAndSpectorServerModel
from schemas import CurrentGameInfo
from utils.wrappers import map_puuid_and_server

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/{server}/match/{match_ID}")
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


@router.post("/{server}/match/{match_ID}")
async def post_match(
    server: SummonerAndSpectorServerModel,
    match_ID: Annotated[str, Path(examples="EUW1_7091585440")],
) -> CurrentGameInfo:
    "Posts data about a specific match from a database"
    pass

    return "Not working"
