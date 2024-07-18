import requests
import logging
import json

from fastapi import HTTPException

from utils.env import API_KEY, DOMAIN_EUROPE

logger = logging.getLogger(__name__)



class AccountController:
    def __init__(self):
        DOMAIN  = DOMAIN_EUROPE + "/riot/account/v1"

        self.URL_GET_ACCOUNT_BY_PUUID = DOMAIN + "/accounts/by-puuid"
        self.URL_GET_ACCOUNT_BY_RIOT_ID = DOMAIN + "/accounts/by-riot-id"
        self.URL_GET_ACTIVE_SHARD_FOR_A_PLAYER = DOMAIN + "active-shard/by-game"
        self.URL_GET_ACCOUNT_BY_ACCES_TOKEN = DOMAIN + "account/me"

        self.router_api_url_puuid = DOMAIN + "/riot/account/v1/accounts/by-puuid"
        self.API_KEY_PARAM = f"?api_key={API_KEY}"

    def get_account_by_puuid(self, puuid: str):
        "Provide summoner's PUUID, get dict of nickname, tag_line and puuid"
        URL = f"{self.URL_GET_ACCOUNT_BY_PUUID}/{puuid}{self.API_KEY_PARAM}"

        response = requests.get(URL)

        if not response.status_code == 200:
            logger.error(f"Could not get summoner puuid. Error: {response.text}. URL: {URL}")
            raise HTTPException(
                status_code=503, detail="Failed to retrieve data from Riot's API"
            )
        
        summoner_info = json.loads(response.text)
        logging.debug(f"get_account_by_puuid > summoner_info: {summoner_info}")

        return summoner_info


    def get_account_by_riot_id(self, summoner_name: str, tag_line: str) -> str:
        "Provide summoner's nickname and tag, get PUUID in return"
        URL = f"{self.URL_GET_ACCOUNT_BY_RIOT_ID}/{summoner_name}/{tag_line}{self.API_KEY_PARAM}"

        response = requests.get(URL)
        if not response.status_code == 200:
            logger.error(f"Could not get summoner puuid. Error: {response.text}. URL: {URL}")
            raise HTTPException(
                status_code=503, detail="Failed to retrieve data from Riot's API"
            )

        raw_data = response.text
        puuid: str = json.loads(raw_data)["puuid"]
        
        logger.debug(f"PUUID {puuid} found for user {summoner_name}#{tag_line}")

        return puuid  

    def get_active_shard_for_a_player(self):
        URL = self.URL_GET_ACTIVE_SHARD_FOR_A_PLAYER
        pass

    def get_account_by_access_token(self):
        URL = self.URL_GET_ACCOUNT_BY_ACCES_TOKEN
        pass