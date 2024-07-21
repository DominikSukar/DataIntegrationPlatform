import os
from dotenv import load_dotenv

load_dotenv()

required_env_vars = [
    "API_KEY",
    "DOMAIN_EUROPE",
    "DOMAIN_AMERICAS",
    "DOMAIN_ASIA",
    "DOMAIN_ESPORTS",
    "DOMAIN_EUW1"
]

env_vars = {var: os.getenv(var) for var in required_env_vars}

missing_vars = [var for var, value in env_vars.items() if not value]
if missing_vars:
    raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")

API_KEY = env_vars["API_KEY"]
DOMAIN_EUROPE = env_vars["DOMAIN_EUROPE"]
DOMAIN_AMERICAS = env_vars["DOMAIN_AMERICAS"]
DOMAIN_ASIA = env_vars["DOMAIN_ASIA"]
DOMAIN_ESPORTS = env_vars["DOMAIN_ESPORTS"]
DOMAIN_EUW1 = env_vars["DOMAIN_EUW1"]
