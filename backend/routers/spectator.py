import logging

from fastapi import APIRouter, HTTPException

from api_requests.account import AccountController
from api_requests.spectator import SpectatorController

from schemas import CurrentGameInfo

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/")
async def get_current_match(nickname: str = None, tag: str = None, puuid: str = None)->CurrentGameInfo:
    "Shows data about current match."
    if not puuid and not (nickname and tag):
        raise HTTPException(
            status_code=400,
            detail="Please provide either puuid or nickname nad tag pair",
        )

    if nickname and tag:
        controller = AccountController()
        puuid = controller.get_account_by_riot_id(nickname, tag)

    controller = SpectatorController()
    match_data = controller.get_current_game_information__for_the_given_puuid(puuid)

    return match_data
