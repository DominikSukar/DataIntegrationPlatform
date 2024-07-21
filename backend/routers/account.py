import logging

from fastapi import APIRouter, HTTPException

from api_requests.account import AccountController

from schemas import AccountDto

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/get_puuid/", status_code=200)
async def get_summoner_puuid(summoner_name: str, tag_line: str) -> str:
    "Return summoner's puuid based on his summoner name and tag line."

    account = AccountController()
    puuid = account.get_account_by_riot_id(summoner_name, tag_line)

    return puuid


@router.get("/info/")
async def get_summoner_info(summoner_name: str = None, tag_line: str = None, puuid: str = None)->AccountDto:
    """
    Returns data about a summoner (puuid, gameName, tagLine) by their nickname+tag or PUUID.
    """
    if not puuid and not (summoner_name and tag_line):
        raise HTTPException(
            status_code=400, detail="Please provide either puuid or nickname nad tag pair"
        )

    account = AccountController()
    if summoner_name and tag_line:
        puuid = account.get_account_by_riot_id(summoner_name, tag_line)
    
    summoner_info = account.get_account_by_puuid(puuid)

    return summoner_info
