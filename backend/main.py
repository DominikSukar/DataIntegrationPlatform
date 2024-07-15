import os
import logging

from fastapi import FastAPI
from dotenv import load_dotenv

from routers import account, match, spectator

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s:      %(message)s",
    handlers=[logging.StreamHandler()],
)
logger = logging.getLogger(__name__)

load_dotenv()
API_KEY = os.getenv("API_KEY")
DOMAIN = os.getenv("DOMAIN")

app = FastAPI()

app.include_router(account.router, prefix="/summoner")
app.include_router(match.router, prefix="/match_history")
app.include_router(spectator.router, prefix="/current_match")
