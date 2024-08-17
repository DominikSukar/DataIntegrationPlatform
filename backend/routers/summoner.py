import logging
from typing import Any

from fastapi import APIRouter, Query
from api_requests.summoner import SummonerControler
from models import SummonerAndSpectorServerModel
from utils.wrappers import map_puuid_and_server

from schemas import SummonerDTO

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/{server}/", status_code=200)
@map_puuid_and_server
async def get_summoner(
    server: SummonerAndSpectorServerModel,
    mapped_server: Any = Query(None, include_in_schema=False),
    summoner_name: str = None,
    puuid: str = None,
) -> SummonerDTO:
    "Return summoner's info based on his PUUID"
    controller = SummonerControler(server)
    summoner = controller.get_a_summoner_by_PUUID(puuid)

    return summoner
