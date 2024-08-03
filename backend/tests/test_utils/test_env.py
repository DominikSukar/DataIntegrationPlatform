import os
from dotenv import load_dotenv

load_dotenv()

REQUIRED_ENV_VARS = [
    "API_KEY",
    "DOMAIN_EUROPE",
    "DOMAIN_AMERICAS",
    "DOMAIN_ASIA",
    "DOMAIN_ESPORTS",
    "DOMAIN_SEA",
    "DOMAIN_BR",
    "DOMAIN_EUNE",
    "DOMAIN_EUW",
    "DOMAIN_JP",
    "DOMAIN_KR",
    "DOMAIN_LAN",
    "DOMAIN_LAS",
    "DOMAIN_ME",
    "DOMAIN_NA",
    "DOMAIN_OCE",
    "DOMAIN_PH",
    "DOMAIN_RU",
    "DOMAIN_SG",
    "DOMAIN_TH",
    "DOMAIN_TR",
    "DOMAIN_TW",
    "DOMAIN_VN",
]


class TestEnvVariables:
    def test_values(self):
        """Tests if all required variables are present and their values are not None"""
        for req_var in REQUIRED_ENV_VARS:
            assert req_var in os.environ
            # Technically it's impossible to have an env var with none/null values on Linux
            assert os.getenv(req_var) is not None
