import logging

from ._base import RiotAPIBase
from models import MatchModel, MatchType
from utils.requests import send_request, send_async_request
from schemas import MatchIds, MatchDto, TimelineDto

logger = logging.getLogger(__name__)


class MatchController(RiotAPIBase):
    "Class manages the Riot's API 'MATCH-V5' service. As of 07.20.2024 there are 3 endpoints."

    PATH = "/lol/match/v5/matches"

    def __init__(self, server: MatchModel):
        domain = super().get_domain(server)
        key = super().KEY
        self.url_list_of_match_ids = "{}{}/by-puuid/{}/ids{}".format(
            domain, self.PATH, "{puuid}", key
        )
        self.url_match = "{}{}/{}{}".format(domain, self.PATH, "{match_id}", key)
        self.url_match_timeline = "{}{}/{}/timeline{}".format(
            domain, self.PATH, "{match_id}", key
        )

    def get_a_list_of_match_ids_by_puuid(
        self, puuid: str, match_type: MatchType, count: int
    ) -> MatchIds:
        "Endpoint gets you a list of user's matches"
        URL = (
            self.url_list_of_match_ids.format(puuid=puuid)
            + f"&type={match_type}&count={count}"
        )
        match_ids = send_request(URL)
        MatchIds.model_validate(match_ids)

        logging.debug(f"get_a_list_of_match_ids_by_puuid > match_ids: {match_ids}")

        return match_ids

    async def get_a_match_by_match_id(self, session, match_id: str) -> MatchDto:
        """Endpoint gets you basic info about a match
        Note: This endpoint is garbage tier, documentation is even worse.
        Turn off validation if necessary"""
        URL = self.url_match.format(match_id=match_id)
        match = await send_async_request(session, URL)
        # MatchDto.model_validate(match)

        # logging.debug(f"get_a_match_by_match_id > match: {match}")

        return match

    async def get_a_match_timeline_by_match_id(self, match_id: str) -> TimelineDto:
        "Endpoint gives you precise timeline of events through the match"
        URL = self.url_match_timeline.format(match_id=match_id)
        match_timeline = send_request(URL)

        return match_timeline
