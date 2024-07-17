import os

from dotenv import load_dotenv

load_dotenv()
API_KEY: str = os.getenv("API_KEY")
DOMAIN_EUROPE: str = os.getenv("DOMAIN_EUROPE")

if not API_KEY or not DOMAIN_EUROPE:
    raise ValueError("API_KEY or DOMAIN_EUROPE is not set in the environment variables")