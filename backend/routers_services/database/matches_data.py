import logging
from typing import List
import aiohttp
import asyncio

from api_requests.match import MatchController
from api_requests.mappers.match import matches_mapper
from serializers.match.match import MatchBase

logger = logging.getLogger(__name__)


async def get_matches_data(
    puuid, mapped_server, match_count, match_type
) -> List[MatchBase]:
    controller = MatchController(server=mapped_server)
    mapped_match_data_list = []

    async with aiohttp.ClientSession() as session:
        match_ids = controller.get_a_list_of_match_ids_by_puuid(
            puuid,
            match_count,
            match_type.value,
        )
        tasks = [
            controller.get_a_match_by_match_id(session, match_id)
            for match_id in match_ids
        ]
        raw_matches = await asyncio.gather(*tasks)

        for raw_match_data in raw_matches:
            match_data_mapped = matches_mapper(raw_match_data, server_id=2, split_id=4)
            mapped_match_data_list.append(match_data_mapped)

    return raw_matches, mapped_match_data_list
