import logging

from fastapi import APIRouter, HTTPException
from models import SummonerAndSpectorServerModel
from api_requests.account import AccountController
from api_requests.spectator import SpectatorController
from schemas import CurrentGameInfo
from utils.wrappers import require_puuid_or_nickname_and_tag

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/")
@require_puuid_or_nickname_and_tag
async def get_current_match(
    server: SummonerAndSpectorServerModel,
    summoner_name: str = None,
    tag_line: str = None,
    puuid: str = None,
) -> CurrentGameInfo:
    "Shows data about current match."
    if not puuid and not (summoner_name and tag_line):
        raise HTTPException(
            status_code=400,
            detail="Please provide either puuid or nickname nad tag pair",
        )

    if summoner_name and tag_line:
        controller = AccountController(server)
        puuid = controller.get_account_by_riot_id(summoner_name, tag_line)

    controller = SpectatorController(server)
    match_data = controller.get_current_game_information__for_the_given_puuid(puuid)

    return match_data
