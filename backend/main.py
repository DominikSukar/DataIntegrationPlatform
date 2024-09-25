import logging
import os

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware

from routers import account, match, spectator, summoner, datadragon, database, server
from middleware import UpperCaseServerParamMiddleware

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

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(account.router, tags=["Account"], prefix="/account")
app.include_router(summoner.router, tags=["Summoner"], prefix="/summoner")
app.include_router(match.router, tags=["Match"], prefix="/match_history")
app.include_router(spectator.router, tags=["Spectator"], prefix="/current_match")
app.include_router(server.router, tags=["Server"], prefix="/server")
app.include_router(database.router, tags=["Database"], prefix="/database")
app.include_router(datadragon.router, tags=["Datadragon"], prefix="/datadragon")
