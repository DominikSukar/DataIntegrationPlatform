import logging
import aiohttp
import asyncio

from fastapi import APIRouter, Query
from models import MatchModel, SummonerAndSpectorServerModel
from api_requests.match import MatchController
from utils.wrappers import map_puuid_and_server

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/{server}/")
@map_puuid_and_server
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
        match_ids = match_ids[:3]

        tasks = [
            controller.get_a_match_by_match_id(session, match_id)
            for match_id in match_ids
        ]
        match_data_list = await asyncio.gather(*tasks)

        data_to_return = []

        for match_data in match_data_list:
            if match_data:
                participants = match_data["info"]["participants"]
                info = match_data["info"]
                metadata = match_data["metadata"]

                team_strc = {}

                for team in info["teams"]:
                    team_ID = "team_1" if team["teamId"] == 100 else "team_2"
                    team_bans = team["bans"]
                    team_objectives = team["objectives"]
                    team_strc[team_ID] = {"bans": team_bans, "objectives": team_objectives}

                info = {
                    "server": server,
                    "matchId": metadata["matchId"],
                    "gameResult": info["endOfGameResult"],
                    "gameDuration": info["gameDuration"],
                    "gameMode": info["gameMode"],
                    "gameType": info["gameType"],
                    "teams": team_strc
                    
                }
                dict_strc = {"info": info,"main_participant": None, "team_1": [], "team_2": []}

                for participant in participants:
                    participant_data = {
                        "server": server,
                        "championName": participant["championName"],
                        "individualPosition": participant["individualPosition"],
                        "teamId": participant["teamId"],
                        "kills": participant["kills"],
                        "deaths": participant["deaths"],
                        "assists": participant["assists"],
                        "summonerName": participant["riotIdGameName"],
                        "tagLine": participant["riotIdTagline"],
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
