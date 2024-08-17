import logging
from typing import Any

from fastapi import APIRouter, Query
from api_requests import SummonerControler, LeagueControler
from models import SummonerAndSpectorServerModel
from utils.wrappers import map_puuid_and_server

from schemas import LeagueAndSummonerEntryDTO

logger = logging.getLogger(__name__)
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
    summoner_controller = SummonerControler(server)
    summoner_data = summoner_controller.get_a_summoner_by_PUUID(puuid)

    league_controller = LeagueControler(server)
    league_data = (
        league_controller.get_league_entries_in_all_queues_for_a_given_summoner_ID(
            summoner_data.id
        )
    )
    summoner_dict = summoner_data.model_dump()
    league_dict = league_data.model_dump()
    print(summoner_dict)
    print(league_dict)
    final_dataset = {**summoner_dict, **league_dict}
    print(final_dataset)

    return final_dataset
