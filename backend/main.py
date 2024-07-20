import logging

from fastapi import FastAPI

from routers import account, match, spectator

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s:      %(message)s",
    handlers=[logging.StreamHandler()],
)
logger = logging.getLogger(__name__)

app = FastAPI()

app.include_router(account.router, tags=["Account"], prefix="/summoner")
app.include_router(match.router, tags=["Match"], prefix="/match_history")
app.include_router(spectator.router, tags=["Spectator"], prefix="/current_match")
