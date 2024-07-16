import os
import requests
import json
import logging

from dotenv import load_dotenv

from fastapi import APIRouter, HTTPException, Query

from models.summoner import SummonerByNickname, SummonerByPUUID

logger = logging.getLogger(__name__)

load_dotenv()
API_KEY: str = os.getenv("API_KEY")
DOMAIN: str = os.getenv("DOMAIN_EUROPE")

if not API_KEY or not DOMAIN:
    raise ValueError("API_KEY or DOMAIN_EUROPE is not set in the environment variables")

router = APIRouter()

router_api_url = DOMAIN + "/riot/account/v1/accounts/by-riot-id"
router_api_url_puuid = DOMAIN + "/riot/account/v1/accounts/by-puuid"
api_key_url = f"?api_key={API_KEY}"


@router.get("/get_puuid/")
def get_summoner_puuid(summoner_name: str, tag_line: str):
    "Returns data about a summoner by their summoner name."
    summoner_url: str = f"{router_api_url}/{summoner_name}/{tag_line}" + api_key_url

    response: str = requests.get(summoner_url)
    if not response.status_code == 200:
        logger.error("Could not get summoner puuid. Error: {}".format(response.text))
        return HTTPException(
            status_code=503, detail="Failed to retrieve data from Riot's API"
        )

    raw_data: str = response.text
    summoner_data = json.loads(raw_data)["puuid"]
    logger.debug(f"PUUID {summoner_data} found for user {summoner_name}#{tag_line}")

    return summoner_data


@router.get("/info/")
async def get_summoner_info(
    nickname: str = Query(None), tag: str = Query(None), puuid: str = Query(None)
):
    """
    Returns data about a summoner by their nickname+tag or PUUID.
    """
    if nickname and tag:
        puuid = get_summoner_puuid(nickname, tag)

    account_info_url = f"{router_api_url_puuid}/{puuid}" + api_key_url

    response: str = requests.get(account_info_url)
    if not response.status_code == 200:
        logger.error(f"Failed to retrieve data from Riot's API. Error: {response.text}. URL: {account_info_url}")
        return HTTPException(
            status_code=503, detail="Failed to retrieve data from Riot's API"
        )

    raw_data: str = response.text
    summoner_info = json.loads(raw_data)

    return summoner_info
