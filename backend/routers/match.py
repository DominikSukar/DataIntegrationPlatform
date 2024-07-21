import logging

from fastapi import APIRouter, HTTPException

from api_requests.account import AccountController
from api_requests.match import MatchController

from schemas import MatchIds, MatchDto

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/")
async def match_history(nickname: str = None, tag: str = None, puuid: str = None):
    """Returns user's match history by provided puuid.
    It is also possible to provide simple nickname and tag,
    however additional request is made by API, making response slower."""
    if not puuid and not (nickname and tag):
        raise HTTPException(
            status_code=400,
            detail="Please provide either puuid or nickname nad tag pair",
        )

    if nickname and tag:
        controller = AccountController()
        puuid = controller.get_account_by_riot_id(nickname, tag)

    controller = MatchController()
    match_ids = controller.get_a_list_of_match_ids_by_puuid(puuid)

    for match_id in match_ids:
        match = controller.get_a_match_by_match_id(match_id)

        return match
