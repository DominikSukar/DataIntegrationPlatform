from logger import get_logger

from ._base import RiotAPIBase
from utils.requests import send_request
from utils.custom_exceptions import MethodUnvailable
from schemas import SummonerDTO, SummonerAndSpectorServerModel

logger = get_logger(__name__)


class SummonerControler(RiotAPIBase):
    "Class manages the Riot's API 'SUMMONER-V4' service. As of 23.07.2024 there are 5 endpoints."

    PATH = "/lol/summoner/v4/summoners"

    def __init__(self, server: SummonerAndSpectorServerModel, puuid: int):
        domain = super().get_domain(server)
        key = super().KEY
        self.url_account_by_puuid = f"{domain}{self.PATH}/by-puuid/{puuid}{key}"

    def get_a_summoner_by_its_RSO_encrypted_PUUID(self) -> SummonerDTO:
        """Not used"""
        raise MethodUnvailable

    def get_a_summoner_by_account_ID(self) -> SummonerDTO:
        """Not used"""
        raise MethodUnvailable

    def get_a_summoner_by_PUUID(self) -> SummonerDTO:
        """Fetches data summoner specific data"""

        URL = self.url_account_by_puuid

        summoner_info = send_request(URL)
        summoner_info = SummonerDTO.model_validate(summoner_info)

        logger.debug(f"get_a_summoner_by_PUUID > summoner_info: {summoner_info}")

        return summoner_info

    def get_a_summoner_by_access_token(self) -> SummonerDTO:
        """Not used"""
        raise MethodUnvailable

    def get_a_summoner_by_summoner_ID(self) -> SummonerDTO:
        """Not used"""
        raise MethodUnvailable
