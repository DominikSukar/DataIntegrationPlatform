import os
from dotenv import load_dotenv

load_dotenv()


def get_var(var_name: str) -> str:
    """Get an environment variable"""
    return os.environ.get(var_name)


API_KEY = get_var("API_KEY")
ITEMS_PATH = get_var("ITEMS_PATH")
SUMMONERS_PATH = get_var("SUMMONERS_PATH")

EUROPE = get_var("DOMAIN_EUROPE")
AMERICAS = get_var("DOMAIN_AMERICAS")
ASIA = get_var("DOMAIN_ASIA")
SEA = get_var("DOMAIN_SEA")
ESPORTS = get_var("DOMAIN_ESPORTS")

BR = get_var("DOMAIN_BR")
EUNE = get_var("DOMAIN_EUNE")
EUW = get_var("DOMAIN_EUW")
JP = get_var("DOMAIN_JP")
KR = get_var("DOMAIN_KR")
LAN = get_var("DOMAIN_LAN")
LAS = get_var("DOMAIN_LAS")
ME = get_var("DOMAIN_ME")
NA = get_var("DOMAIN_NA")
OCE = get_var("DOMAIN_OCE")
PH = get_var("DOMAIN_PH")
RU = get_var("DOMAIN_RU")
SG = get_var("DOMAIN_SG")
TH = get_var("DOMAIN_TH")
TR = get_var("DOMAIN_TR")
TW = get_var("DOMAIN_TW")
VN = get_var("DOMAIN_VN")
