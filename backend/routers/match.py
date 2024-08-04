import logging
import aiohttp
import asyncio

from fastapi import APIRouter, Query
from models import MatchModel, SummonerAndSpectorServerModel
from api_requests.match import MatchController
from utils.wrappers import require_puuid_or_nickname_and_tag

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/")
@require_puuid_or_nickname_and_tag
async def match_history(
    server: SummonerAndSpectorServerModel,
    mapped_server: MatchModel = Query(None, include_in_schema=False),
    summoner_name: str = None,
    puuid: str = None,
):
    """Returns user's match history by provided puuid."""
    controller = MatchController(mapped_server)

    async with aiohttp.ClientSession() as session:
        match_ids = controller.get_a_list_of_match_ids_by_puuid(puuid)
        match_ids = match_ids[:5]

        tasks = [
            controller.get_a_match_by_match_id(session, match_id)
            for match_id in match_ids
        ]
        match_data_list = await asyncio.gather(*tasks)

        data_to_return = []

        for match_data in match_data_list:
            if match_data:
                participants = match_data["info"]["participants"]

                dict_strc = {"main_participant": None, "team_1": [], "team_2": []}

                for participant in participants:
                    participant_data = {
                        "championId": participant["championId"],
                        "championName": participant["championName"],
                        "individualPosition": participant["individualPosition"],
                        "teamId": participant["teamId"],
                        "kills": participant["kills"],
                        "deaths": participant["deaths"],
                        "assists": participant["assists"],
                    }
                    if participant["puuid"] == puuid:
                        dict_strc["main_participant"] = {
                            **participant_data,
                            "win": participant["win"],
                            "timePlayed": participant["timePlayed"],
                        }

                    team_key = "team_1" if participant["teamId"] == 100 else "team_2"
                    dict_strc[team_key].append(participant_data)

                data_to_return.append(dict_strc)

        return data_to_return
