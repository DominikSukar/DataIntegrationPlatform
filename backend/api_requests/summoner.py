import logging

from ._base import RiotAPIBase
from models import SummonerAndSpectorServerModel
from utils.requests import send_request
from schemas import SummonerDTO

logger = logging.getLogger(__name__)


class SummonerControler(RiotAPIBase):
    "Class manages the Riot's API 'SUMMONER-V4' service. As of 23.07.2024 there are 5 endpoints."

    PATH = "/lol/summoner/v4/summoners"

    def __init__(self, server: SummonerAndSpectorServerModel):
        super().__init__(server, SummonerAndSpectorServerModel)
        domain = super().get_domain(self.server)
        key = super().KEY
        self.url_account_by_puuid = "{}{}/by-puuid/{}{}".format(
            domain, self.PATH, "{puuid}", key
        )

    def get_a_summoner_by_its_RSO_encrypted_PUUID(self) -> SummonerDTO:
        """Not used"""
        URL = self.url_account_by_access_token
        pass

    def get_a_summoner_by_account_ID(self) -> SummonerDTO:
        """Not used"""
        URL = self.url_account_by_access_token
        pass

    def get_a_summoner_by_PUUID(self, puuid: str) -> SummonerDTO:
        """Fetches data summoner specific data"""

        URL = self.url_account_by_puuid.format(puuid=puuid)

        summoner_info = send_request(URL)
        summoner_info = SummonerDTO.model_validate(summoner_info)

        logging.debug(f"get_a_summoner_by_PUUID > summoner_info: {summoner_info}")

        return summoner_info

    def get_a_summoner_by_access_token(self) -> SummonerDTO:
        """Not used"""
        URL = self.url_account_by_access_token
        pass

    def get_a_summoner_by_summoner_ID(self) -> SummonerDTO:
        """Not used"""
        URL = self.url_account_by_access_token
        pass
