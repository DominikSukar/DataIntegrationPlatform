import logging
import time
import aiohttp
import asyncio

from fastapi import APIRouter, HTTPException

from api_requests.account import AccountController
from api_requests.match import MatchController

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/")
async def match_history(nickname: str = None, tag: str = None, puuid: str = None):
    """Returns user's match history by provided puuid.
    It is also possible to provide simple nickname and tag,
    however additional request is made by API, making response slower."""
    start_time = time.time()

    if not puuid and not (nickname and tag):
        raise HTTPException(
            status_code=400,
            detail="Please provide either puuid or nickname nad tag pair",
        )

    if nickname and tag:
        controller = AccountController()
        puuid = controller.get_account_by_riot_id(nickname, tag)

    controller = MatchController()

    async with aiohttp.ClientSession() as session:
        match_ids = controller.get_a_list_of_match_ids_by_puuid(puuid)
        match_ids = match_ids[:5]

        time_before_fetching = time.time() - start_time

        tasks = [
            controller.get_a_match_by_match_id(session, match_id)
            for match_id in match_ids
        ]
        match_data_list = await asyncio.gather(*tasks)

        data_to_return = []

        for match_data in match_data_list:
            if match_data:
                participants = match_data["info"]["participants"]

                matched_participant = next(
                    (
                        {
                            "win": participant["win"],
                            "championId": participant["championId"],
                            "championName": participant["championName"],
                            "individualPosition": participant["individualPosition"],
                            "teamId": participant["teamId"],
                        }
                        for participant in participants
                        if participant["puuid"] == puuid
                    ),
                    None,
                )

                if matched_participant:
                    data_to_return.append(matched_participant)

        process_time = time.time() - start_time
        data_to_return.insert(
            0, {"time": process_time, "time_before_fetching": time_before_fetching}
        )

        return data_to_return
