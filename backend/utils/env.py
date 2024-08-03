import os
from dotenv import load_dotenv

load_dotenv()


def get_var(var_name: str) -> str:
    """Get an environment variable"""
    return os.environ.get(var_name)


API_KEY = get_var("API_KEY")

DOMAIN_EUROPE = get_var("DOMAIN_EUROPE")
DOMAIN_AMERICAS = get_var("DOMAIN_AMERICAS")
DOMAIN_ASIA = get_var("DOMAIN_ASIA")
DOMAIN_SEA = get_var("DOMAIN_SEA")
DOMAIN_ESPORTS = get_var("DOMAIN_ESPORTS")

DOMAIN_BR = get_var("DOMAIN_BR")
DOMAIN_EUNE = get_var("DOMAIN_EUNE")
DOMAIN_EUW = get_var("DOMAIN_EUW")
DOMAIN_JP = get_var("DOMAIN_JP")
DOMAIN_KR = get_var("DOMAIN_KR")
DOMAIN_LAN = get_var("DOMAIN_LAN")
DOMAIN_LAS = get_var("DOMAIN_LAS")
DOMAIN_ME = get_var("DOMAIN_ME")
DOMAIN_NA = get_var("DOMAIN_NA")
DOMAIN_OCE = get_var("DOMAIN_OCE")
DOMAIN_PH = get_var("DOMAIN_PH")
DOMAIN_RU = get_var("DOMAIN_RU")
DOMAIN_SG = get_var("DOMAIN_SG")
DOMAIN_TH = get_var("DOMAIN_TH")
DOMAIN_TR = get_var("DOMAIN_TR")
DOMAIN_TW = get_var("DOMAIN_TW")
DOMAIN_VN = get_var("DOMAIN_VN")
