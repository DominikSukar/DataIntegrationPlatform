import logging

from ._base import RiotAPIBase
from models import SummonerAndSpectorServerModel
from utils.requests import send_request
from schemas import LeagueEntryDTO

logger = logging.getLogger(__name__)


class SummonerControler(RiotAPIBase):
    "Class manages the Riot's API 'LEAGUE-V4' service. As of 18.08.2024 there are 6 endpoints."

    PATH = "/lol/league/v4/entries"

    def __init__(self, server: SummonerAndSpectorServerModel):
        domain = super().get_domain(server)
        key = super().KEY
        self.url_league_entries_for_ID = "{}{}/by-summoner/{}{}".format(
            domain, self.PATH, "{summoner_id}", key
        )

    def get_the_challenger_league_for_given_queue(self):
        """Not used"""
        pass

    def get_league_entries_in_all_queues_for_a_given_summoner_ID(
        self, summoner_id: str
    ) -> LeagueEntryDTO:
        """Fetches ranked data"""

        URL = self.url_account_by_puuid.format(summoner_id=summoner_id)

        summoner_info = send_request(URL)
        summoner_info = LeagueEntryDTO.model_validate(summoner_info)

        logging.debug(
            f"get_league_entries_in_all_queues_for_a_given_summoner_ID > summoner_info: {summoner_info}"
        )

        return summoner_info

    def get_all_the_league_entries(self, puuid: str):
        """Not used"""

    def get_the_grandmaster_league_of_a_specific_queue(self):
        """Not used"""
        pass

    def get_league_with_given_ID_including_inactive_entries(self):
        """Not used"""
        pass

    def get_the_master_league_for_given_queue(self):
        """Not used"""
        pass
