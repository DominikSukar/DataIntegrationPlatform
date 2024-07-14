import os
import requests
import json

from typing import List

from dotenv import load_dotenv

from fastapi import APIRouter, HTTPException

load_dotenv()
API_KEY = os.getenv('API_KEY')
DOMAIN = os.getenv('DOMAIN_EUROPE')

router = APIRouter()

router_api_url = DOMAIN + "/lol/match/v5/matches/by-puuid"
api_key_url = f"?api_key={API_KEY}"

@router.get('/{puuid}')
def match_history(puuid: str):
    "Returns data about matches of a user's provided puuid."
    match_list_url: str = f"{router_api_url}/{puuid}/ids" + api_key_url

    response: str = requests.get(match_list_url)
    if not response.status_code == 200:
        return HTTPException(status_code=503, detail="Failed to retrieve data from Riot's API")
    
    raw_data: str = response.text
    match_ids: List[str] = json.loads(raw_data)
    
    for match_id in match_ids:
        match_url = f"{DOMAIN}/lol/match/v5/matches/{match_id}?api_key={API_KEY}"
        raw_data = requests.get(match_url).text
        match_data = json.loads(raw_data)
        return match_data