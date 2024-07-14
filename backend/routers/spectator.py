import os
import requests
import json

from dotenv import load_dotenv

from fastapi import APIRouter, HTTPException

load_dotenv()
API_KEY = os.getenv('API_KEY')
DOMAIN = os.getenv('DOMAIN_EUROPE')

router = APIRouter()
router_api_url = DOMAIN + "/lol/spectator/v5/active-games/by-summoner"
api_key_url = f"?api_key={API_KEY}"

@router.get('/current_match/{puuid}')
def get_current_match(puuid: str):
    "Shows data about current match."
    current_match_url: str = f"{router_api_url}/{puuid}" + api_key_url

    response: str = requests.get(current_match_url)
    if not response.status_code == 200:
        return HTTPException(status_code=503, detail="Failed to retrieve data from Riot's API")
    
    raw_data: str = response.text    
    match_data = json.loads(raw_data)

    return match_data
