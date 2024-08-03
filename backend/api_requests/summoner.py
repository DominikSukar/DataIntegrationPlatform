import logging

from utils.env import API_KEY, EUW
from utils.requests import send_request

from schemas import SummonerDTO

logger = logging.getLogger(__name__)


class SummonerControler:
    "Class manages the Riot's API 'SUMMONER-V4' service. As of 23.07.2024 there are 5 endpoints."

    DOMAIN = EUW + "/lol/summoner/v4/summoners"
    key = f"?api_key={API_KEY}"

    url_account_by_puuid = "{}/by-puuid/{}{}".format(DOMAIN, "{puuid}", key)

    def get_a_summoner_by_its_RSO_encrypted_PUUID(self)->SummonerDTO:
        """Not used"""
        URL = self.url_account_by_access_token
        pass

    
    def get_a_summoner_by_account_ID(self)->SummonerDTO:
        """Not used"""
        URL = self.url_account_by_access_token
        pass

    
    def get_a_summoner_by_PUUID(self, puuid: str)->SummonerDTO:
        """Fetches data summoner specific data"""

        URL = self.url_account_by_puuid.format(puuid=puuid)

        summoner_info = send_request(URL)
        summoner_info = SummonerDTO.model_validate(summoner_info)

        logging.debug(f"get_a_summoner_by_PUUID > summoner_info: {summoner_info}")

        return summoner_info

    
    def get_a_summoner_by_access_token(self)->SummonerDTO:
        """Not used"""
        URL = self.url_account_by_access_token
        pass

    
    def get_a_summoner_by_summoner_ID(self)->SummonerDTO:
        """Not used"""
        URL = self.url_account_by_access_token
        pass
