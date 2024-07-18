import os
import requests
import json
import logging

from dotenv import load_dotenv

from fastapi import APIRouter, HTTPException, Query

from models.summoner import SummonerByNickname, SummonerByPUUID
from api_requests.account import AccountController

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
async def get_summoner_puuid(summoner_name: str, tag_line: str) -> str:
    "Return summoner's puuid based on his summoner name and tag line."
    account = AccountController()
    puuid = account.get_account_by_riot_id(summoner_name, tag_line)

    return puuid


@router.get("/info/")
async def get_summoner_info(nickname: str = None, tag: str = None, puuid: str = None):
    """
    Returns data about a summoner by their nickname+tag or PUUID.
    """
    if not puuid and not (nickname and tag):
        raise HTTPException(
            status_code=400, detail="Please provide either puuid or nickname nad tag pair"
        )

    account = AccountController()
    if nickname and tag:
        puuid = account.get_account_by_riot_id(nickname, tag)
    
    summoner_info = account.get_account_by_puuid(puuid)

    return summoner_info
