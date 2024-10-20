from typing import Any

from fastapi import APIRouter, Query

from logger import get_logger
from api_requests import SummonerControler, LeagueControler
from models import SummonerAndSpectorServerModel
from utils.wrappers.mappers import map_puuid_and_server
from schemas import LeagueAndSummonerEntryDTO

logger = get_logger(__name__)
router = APIRouter()


@router.get("/{server}/", status_code=200)
@map_puuid_and_server
async def get_summoner(
    server: SummonerAndSpectorServerModel,
    mapped_server: Any = Query(None, include_in_schema=False),
    summoner_name: str = None,
    puuid: str = None,
) -> LeagueAndSummonerEntryDTO:
    "Return summoner's info based on his PUUID"
    summoner_controller = SummonerControler(server, puuid)
    summoner_data = summoner_controller.get_a_summoner_by_PUUID()

    league_controller = LeagueControler(server)

    league_data = (
        league_controller.get_league_entries_in_all_queues_for_a_given_summoner_ID(
            summoner_data.id
        )
    )

    summoner_dict = summoner_data.model_dump()
    league_dict = league_data.model_dump()
    if league_dict["losses"] == 0 and league_dict["wins"] == 0:
        winrate = 0
    else:
        winrate = league_dict["wins"] / (league_dict["wins"] + league_dict["losses"])
    league_dict["winrate"] = int(winrate * 100)
    final_dataset = {**summoner_dict, **league_dict}

    final_dataset = LeagueAndSummonerEntryDTO.model_validate(final_dataset)

    return final_dataset
