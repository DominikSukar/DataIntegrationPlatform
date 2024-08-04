import logging
from typing import Any

from fastapi import APIRouter, Query
from models import SummonerAndSpectorServerModel
from api_requests.spectator import SpectatorController
from schemas import CurrentGameInfo
from utils.wrappers import map_puuid_and_server

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/")
@map_puuid_and_server
async def get_current_match(
    server: SummonerAndSpectorServerModel,
    mapped_server: Any = Query(None, include_in_schema=False),
    summoner_name: str = None,
    puuid: str = None,
) -> CurrentGameInfo:
    "Shows data about current match."
    controller = SpectatorController(server)
    match_data = controller.get_current_game_information__for_the_given_puuid(puuid)

    return match_data
