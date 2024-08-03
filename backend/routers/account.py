import logging

from fastapi import APIRouter

from api_requests.account import AccountController
from utils.wrappers import require_puuid_or_nickname_and_tag

from models import AccountModel
from schemas import AccountDto

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/get_puuid/", status_code=200)
async def get_account_puuid(
    server: AccountModel, summoner_name: str, tag_line: str
) -> str:
    "Return account's puuid based on his account name and tag line."

    controller = AccountController(server)
    puuid = controller.get_account_by_riot_id(summoner_name, tag_line)

    return puuid


@router.get("/info/")
@require_puuid_or_nickname_and_tag
async def get_account_info(
    server: AccountModel, summoner_name: str = None, tag_line: str = None, puuid: str = None
) -> AccountDto:
    """
    Returns data about a account (puuid, gameName, tagLine) by their nickname+tag or PUUID.
    """

    controller = AccountController(server)
    if summoner_name and tag_line:
        puuid = controller.get_account_by_riot_id(summoner_name, tag_line)

    summoner_info = controller.get_account_by_puuid(puuid)

    return summoner_info
