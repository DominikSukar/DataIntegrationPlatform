import os

from dotenv import load_dotenv

load_dotenv()
API_KEY: str = os.getenv("API_KEY")
DOMAIN: str = os.getenv("DOMAIN_EUROPE")

if not API_KEY or not DOMAIN:
    raise ValueError("API_KEY or DOMAIN_EUROPE is not set in the environment variables")

router_api_url = DOMAIN + "/riot/account/v1/accounts/by-riot-id"
router_api_url_puuid = DOMAIN + "/riot/account/v1/accounts/by-puuid"
api_key_url = f"?api_key={API_KEY}"

def get_account_by_puuid():
    pass

def get_account_by_riot_id():
    pass

def get_active_shard_for_a_player():
    pass

def get_account_by_access_token():
    pass