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
api_key_url = f"?api_key={API_KEY}"


@router.get("/get_puuid/")
def get_summoner_puuid(summoner_name: str, tag_line: str):
    "Returns data about a summoner by their summoner name."
    summoner_url: str = f"{router_api_url}/{summoner_name}/{tag_line}" + api_key_url

    response: str = requests.get(summoner_url)
    if not response.status_code == 200:
        return HTTPException(
            status_code=503, detail="Failed to retrieve data from Riot's API"
        )

    raw_data: str = response.text
    summoner_data = json.loads(raw_data)["puuid"]

    return summoner_data


@router.get("/puuid/")
async def get_summoner(
    nickname: str = Query(None), tag: str = Query(None), puuid: str = Query(None)
):
    """
    Returns data about a summoner by their nickname+tag or PUUID.
    """
    if nickname and tag:
        print("if")
    elif puuid:
        print("elif")
    else:
        print("else")

    return "Yeah bro"
