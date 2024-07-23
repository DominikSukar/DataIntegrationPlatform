import logging

from fastapi import APIRouter, HTTPException

from api_requests.account import AccountController
from api_requests.summoner import SummonerControler

from schemas import SummonerDTO

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/", status_code=200)
async def get_summoner(summoner_name: str = None, tag_line: str = None, puuid: str = None) -> SummonerDTO:
    "Return summoner's info based on his PUUID"
    if not puuid and not (summoner_name and tag_line):
        raise HTTPException(
            status_code=400, detail="Please provide either puuid or nickname nad tag pair"
        )
    
    if summoner_name and tag_line:
        controller = AccountController()
        puuid = controller.get_account_by_riot_id(summoner_name, tag_line)

    controller = SummonerControler()
    summoner = controller.get_a_summoner_by_PUUID(puuid)

    return summoner

