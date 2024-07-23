import logging
import requests

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import account, match, spectator, summoner

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s:      %(message)s",
    handlers=[logging.StreamHandler()],
)
logging.getLogger("requests").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(account.router, tags=["Account"], prefix="/account")
app.include_router(summoner.router, tags=["Summoner"], prefix="/summoner")
app.include_router(match.router, tags=["Match"], prefix="/match_history")
app.include_router(spectator.router, tags=["Spectator"], prefix="/current_match")

