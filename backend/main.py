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

app.include_router(account.router, prefix="/summoner")
app.include_router(match.router, prefix="/match_history")
app.include_router(spectator.router, prefix="/current_match")
