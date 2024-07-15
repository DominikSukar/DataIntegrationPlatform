import os
import requests
import json
import logging

from dotenv import load_dotenv

from fastapi import APIRouter, HTTPException, Query

from .account import get_summoner_puuid

logger = logging.getLogger(__name__)

load_dotenv()
API_KEY = os.getenv("API_KEY")
DOMAIN = os.getenv("DOMAIN_EUW1")

router = APIRouter()
router_api_url = DOMAIN + "/lol/spectator/v5/active-games/by-summoner"
api_key_url = f"?api_key={API_KEY}"


@router.get("/")
def get_current_match(
    nickname: str = Query(None), tag: str = Query(None), puuid: str = Query(None)
):
    "Shows data about current match."

    if nickname and tag:
        puuid = get_summoner_puuid(nickname, tag)

    current_match_url: str = f"{router_api_url}/{puuid}" + api_key_url

    response: str = requests.get(current_match_url)
    if not response.status_code == 200:
        logger.error(f"Failed to retrieve data from Riot's API. Error: {response.text}. URL: {current_match_url}")
        return HTTPException(
            status_code=503, detail="Failed to retrieve data from Riot's API"
        )

    raw_data: str = response.text
    match_data = json.loads(raw_data)

    return match_data
