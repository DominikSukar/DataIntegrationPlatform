from logger import get_logger

from fastapi import APIRouter, Query

from api_requests.account import AccountController
from utils.wrappers import map_puuid_and_server, map_server

from models import AccountModel, SummonerAndSpectorServerModel
from schemas import AccountDto

logger = get_logger(__name__)
router = APIRouter()


@router.get("/{server}/get_puuid/", status_code=200)
@map_server
async def get_account_puuid(
    summoner_name: str,
    tag_line: str,
    server: SummonerAndSpectorServerModel,
    mapped_server: AccountModel = Query(None, include_in_schema=False),
) -> str:
    "Return account's puuid based on his account name and tag line."

    controller = AccountController(mapped_server)
    puuid = controller.get_account_by_riot_id(summoner_name, tag_line)

    return puuid


@router.get("/{server}/info/")
@map_puuid_and_server
async def get_account_info(
    server: SummonerAndSpectorServerModel,
    mapped_server: AccountModel = Query(None, include_in_schema=False),
    summoner_name: str = None,
    puuid: str = None,
) -> AccountDto:
    """
    Returns data about a account (puuid, gameName, tagLine) by their nickname+tag or PUUID.

    WARNING: Both "server" and "mapped_server" variables are accessable thanks to decorator
    """

    controller = AccountController(mapped_server)
    summoner_info = controller.get_account_by_puuid(puuid)

    return summoner_info
