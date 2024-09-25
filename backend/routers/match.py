import logging
import aiohttp
import asyncio
from typing import Annotated

from fastapi import APIRouter, Query, Path
from models import MatchModel, MatchType, SummonerAndSpectorServerModel
from api_requests.match import MatchController
from .summoner import get_summoner
from utils.wrappers import map_puuid_and_server

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/{server}/{match_ID}")
@map_puuid_and_server
async def match_timeline(
    server: SummonerAndSpectorServerModel,
    match_ID: Annotated[str, Path(examples="EUW1_7091585440")],
    mapped_server: MatchModel = Query(None, include_in_schema=False),
    summoner_name: str = None,
    puuid: str = None,
):
    pass


@router.get("/{server}/")
@map_puuid_and_server
async def match_history(
    server: SummonerAndSpectorServerModel,
    match_type: Annotated[
        MatchType,
        Query(
            title="Query string",
            description="""Filter the list of match ids by the type of match. This filter is mutually inclusive of the queue filter meaning any match ids returned must match both the queue and type filters.
        Default value is ranked, so not need to pass it. Do not use '--', it's FastAPI/enum bug.""",
        ),
    ] = MatchType.ranked,
    mapped_server: MatchModel = Query(None, include_in_schema=False),
    summoner_name: str = None,
    puuid: str = None,
    count: int = Query(
        3,
        ge=0,
        le=100,
        description="Defaults to 3. Valid values: 0 to 100. Number of match ids to return.",
    ),
):
    """Returns user's match history by provided puuid."""
    data = get_summoner(
        server=server,
        summoner_name=summoner_name if summoner_name else None,
        puuid=puuid if puuid else None,
    )
    await data
    controller = MatchController(mapped_server)

    async with aiohttp.ClientSession() as session:
        match_ids = controller.get_a_list_of_match_ids_by_puuid(
            puuid, match_type.value, count
        )

        tasks = [
            controller.get_a_match_by_match_id(session, match_id)
            for match_id in match_ids
        ]
        match_data_list = await asyncio.gather(*tasks)

        if not match_data_list:
            raise ValueError("No data found")

        data_to_return = []

        for match_data in match_data_list:
            if match_data:
                participants = match_data["info"]["participants"]
                metadata = match_data["metadata"]

                team_strc = {}

                for team in match_data["info"]["teams"]:
                    team_ID = "team_1" if team["teamId"] == 100 else "team_2"
                    team_bans = team["bans"]
                    team_objectives = team["objectives"]
                    team_strc[team_ID] = {
                        "bans": team_bans,
                        "objectives": team_objectives,
                    }
                try:
                    game_info = {
                        "server": server,
                        "endOfGameResult": match_data["info"]["endOfGameResult"],
                        "matchId": metadata["matchId"],
                        "gameEndTimestamp": match_data["info"]["gameEndTimestamp"],
                        "gameDuration": match_data["info"]["gameDuration"],
                        "gameMode": match_data["info"]["gameMode"],
                        "gameType": match_data["info"]["gameType"],
                        "teams": team_strc,
                    }
                except Exception:
                    del match_data["info"]["participants"]
                    del match_data["info"]["teams"]
                    raise ValueError(match_data)
                if not match_data["info"]["gameMode"] == "ARAM":
                    game_info["gameResult"] = match_data["info"]["endOfGameResult"]

                dict_strc = {
                    "info": game_info,
                    "main_participant": None,
                    "team_1": [],
                    "team_2": [],
                }

                for participant in participants:
                    kills = participant["kills"]
                    assists = participant["assists"]
                    deaths = participant["deaths"]
                    if not deaths == 0:
                        kda = (kills + assists) / deaths
                        kda = "{:.2f}".format(kda)
                    elif deaths == 0 and kills == 0 and assists == 0:
                        kda = "0.00"
                    else:
                        kda = "Perfect"

                    for style in participant["perks"]["styles"]:
                        if style["description"] == "primaryStyle":
                            primary_perks = [
                                perk["perk"] for perk in style["selections"]
                            ]
                            primary_style = style["style"]
                        elif style["description"] == "subStyle":
                            secondary_perks = [
                                perk["perk"] for perk in style["selections"]
                            ]
                            secondary_style = style["style"]

                    participant_data = {
                        "championName": participant["championName"],
                        "individualPosition": participant["individualPosition"],
                        "teamId": participant["teamId"],
                        "kills": kills,
                        "deaths": deaths,
                        "assists": assists,
                        "kda": kda,
                        "kp": (
                            int(participant["challenges"]["killParticipation"] * 100)
                            if participant["challenges"].get("killParticipation")
                            is not None
                            else 0
                        ),
                        "summonerName": participant["riotIdGameName"],
                        "tagLine": participant["riotIdTagline"],
                        "items": [
                            participant["item0"],
                            participant["item1"],
                            participant["item2"],
                            participant["item3"],
                            participant["item4"],
                            participant["item5"],
                            participant["item6"],
                        ],
                        "summoners": [
                            participant["summoner1Id"],
                            participant["summoner2Id"],
                        ],
                        "perks": {
                            "primary": {
                                "style": primary_style,
                                "perks": primary_perks,
                            },
                            "secondary": {
                                "style": secondary_style,
                                "perks": secondary_perks,
                            },
                        },
                        "visionScore": participant["visionScore"],
                        "isMain": False,
                    }

                    if participant["puuid"] == puuid:
                        dict_strc["main_participant"] = {
                            **participant_data,
                            "win": participant["win"],
                            "timePlayed": participant["timePlayed"],
                        }
                        participant_data["isMain"] = True
                        game_result = "Win" if participant["win"] else "Defeat"
                        if match_data["info"]["gameDuration"] < 200:
                            game_result = "Remake"
                        dict_strc["info"]["gameResult"] = game_result

                    team_key = "team_1" if participant["teamId"] == 100 else "team_2"
                    dict_strc[team_key].append(participant_data)

                data_to_return.append(dict_strc)

        return data_to_return
