import os

from logger import configure_logger, get_logger

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware

from routers import (
    account,
    match,
    spectator,
    summoner,
    datadragon,
    database,
    servers,
    items,
    champions,
    summoner_spells,
    perks,
    seasons,
    splits,
)
from middleware import UpperCaseServerParamMiddleware

configure_logger()
logger = get_logger(__name__)

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

app.add_middleware(
    BaseHTTPMiddleware,
    dispatch=UpperCaseServerParamMiddleware(
        some_attribute="some_attribute_here_if_needed"
    ),
)

if os.path.exists("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")
else:
    logger.warning(
        "Directory with static content has not been found. The endpoints will not work."
    )

app.include_router(account.router, tags=["Account"], prefix="/account")
app.include_router(summoner.router, tags=["Summoner"], prefix="/summoner")
app.include_router(match.router, tags=["Match"], prefix="/match_history")
app.include_router(spectator.router, tags=["Spectator"], prefix="/current_match")
app.include_router(servers.router, tags=["Servers"], prefix="/servers")
app.include_router(items.router, tags=["Items"], prefix="/items")
app.include_router(perks.router, tags=["Perks"], prefix="/perks")
app.include_router(
    summoner_spells.router, tags=["Summoner spells"], prefix="/summoner_spells"
)
app.include_router(champions.router, tags=["Champions"], prefix="/champions")
app.include_router(seasons.router, tags=["Seasons"], prefix="/seasons")
app.include_router(splits.router, tags=["Splits"], prefix="/splits")
app.include_router(database.router, tags=["Database"], prefix="/database")
app.include_router(
    datadragon.router, tags=["Datadragon"], prefix="/datadragon", deprecated=True
)
