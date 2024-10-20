from typing import List
import aiohttp
import asyncio

from logger import get_logger
from api_requests.match import MatchController
from serializers.match.match import MatchBase

logger = get_logger(__name__)


async def get_matches_ids(
    puuid: str, mapped_server: str, match_count: int, match_type: str, start_time: int
) -> List[str]:
    "Fetching IDs of matches that provided puuid has participated in from Riot API"
    controller = MatchController(server=mapped_server)

    match_ids = controller.get_a_list_of_match_ids_by_puuid(
        puuid, match_count, match_type.value, start_time
    )

    logger.debug(f"Fetched match ids: {len(match_ids) = }")

    return match_ids


async def get_matches_data(mapped_server: str, match_ids: List[str]) -> List[MatchBase]:
    "Fetching data of matches based on provided list of match ids from Riot API"
    controller = MatchController(server=mapped_server)
    async with aiohttp.ClientSession() as session:
        tasks = [
            controller.get_a_match_by_match_id(session, match_id)
            for match_id in match_ids
        ]
        raw_matches = await asyncio.gather(*tasks)

    logger.debug(f"Fetched matches: {len(raw_matches) = }")

    return raw_matches
