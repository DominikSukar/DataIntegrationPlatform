import logging
import requests

from fastapi import FastAPI

from routers import account, match, spectator, summoner

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s:      %(message)s",
    handlers=[logging.StreamHandler()],
)
logging.getLogger("requests").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

app = FastAPI()

app.include_router(account.router, tags=["Account"], prefix="/account")
app.include_router(summoner.router, tags=["Summoner"], prefix="/summoner")
app.include_router(match.router, tags=["Match"], prefix="/match_history")
app.include_router(spectator.router, tags=["Spectator"], prefix="/current_match")

