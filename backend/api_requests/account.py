import requests
import logging
import json

from fastapi import HTTPException

from utils.env import API_KEY, DOMAIN_EUROPE

logger = logging.getLogger(__name__)

DOMAIN  = DOMAIN_EUROPE + "/riot/account/v1"

URL_GET_ACCOUNT_BY_PUUID = DOMAIN + "/accounts/by-puuid"
URL_GET_ACCOUNT_BY_RIOT_ID = DOMAIN + "/accounts/by-riot-id"
URL_GET_ACTIVE_SHARD_FOR_A_PLAYER = DOMAIN + "active-shard/by-game"
URL_GET_ACCOUNT_BY_ACCES_TOKEN = DOMAIN + "account/me"

router_api_url_puuid = DOMAIN + "/riot/account/v1/accounts/by-puuid"
API_KEY = f"?api_key={API_KEY}"

def get_account_by_puuid(puuid: str):
    "Provide summoner's PUUID, get dict of nickname, tag_line and puuid"
    URL = URL_GET_ACCOUNT_BY_PUUID + "/" + puuid + API_KEY

    response = requests.get(URL)

    if not response.status_code == 200:
        logger.error(f"Could not get summoner puuid. Error: {response.text}. URL: {URL}")
        raise HTTPException(
            status_code=503, detail="Failed to retrieve data from Riot's API"
        )
    
    summoner_info = json.loads(response.text)
    logging.info(f"get_account_by_puuid > summoner_info: {summoner_info}")

    return summoner_info


def get_account_by_riot_id(summoner_name: str, tag_line: str) -> str:
    "Provide summoner's nickname and tag, get PUUID in return"
    URL = URL_GET_ACCOUNT_BY_RIOT_ID + f"/{summoner_name}/{tag_line}" + API_KEY

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

def get_active_shard_for_a_player():
    URL = URL_GET_ACTIVE_SHARD_FOR_A_PLAYER
    pass

def get_account_by_access_token():
    URL = URL_GET_ACCOUNT_BY_ACCES_TOKEN
    pass