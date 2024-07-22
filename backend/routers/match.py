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
    NUM_OF_GAMES_TO_FETCH = 20

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
    
    data_to_return = []

    for match_id in match_ids:
        match_data = controller.get_a_match_by_match_id(match_id)

        participants = match_data["info"]["participants"]
        
        for participant in participants:
            if participant["puuid"] == puuid:
                matched_participant = {
                    "win": participant["win"],
                    "championId": participant["championId"],
                    "championName": participant["championName"],
                    "individualPosition": participant["individualPosition"],
                    "teamId": participant["teamId"],
                }
                break

        data_to_return.append(matched_participant)

    return data_to_return
