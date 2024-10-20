from functools import wraps
from fastapi import HTTPException
from typing import Callable
import time

from models import AccountModel, MatchModel, SummonerAndSpectorServerModel
from api_requests.account import AccountController
from utils.domain_routers import get_mapped_server
from logger import get_logger

logger = get_logger(__name__)


def map_server(func: Callable) -> Callable:
    @wraps(func)
    async def wrapper(*args, **kwargs):
        server = kwargs.get("server")
        "Check if our server is of multi-type SummonerAndSpectorServerModel, so EUW, EUNE, NA, etc"
        if isinstance(server, SummonerAndSpectorServerModel):
            "Create var that will be used to determine whether we are dealing with a main server (EUROPE, ASIA etc) or minor server (EUW, EUNE, KR)"
            mapped_server = get_mapped_server(server)
        else:
            "If not then check if its either of type AccountModel (without SEA) or MatchModel (without ESPORTS)"
            if isinstance(server, AccountModel):
                pass
            if isinstance(server, MatchModel):
                pass

        kwargs.pop("mapped_server", None)

        return await func(mapped_server=mapped_server, *args, **kwargs)

    return wrapper


def map_puuid_and_server(func: Callable) -> Callable:
    @wraps(func)
    async def wrapper(*args, **kwargs):
        # Extract parameters from kwargs
        puuid = kwargs.get("puuid")
        summoner_name = kwargs.get("summoner_name")
        server = kwargs.get("server")

        if not puuid and not summoner_name:
            raise HTTPException(
                status_code=400,
                detail="Please provide either puuid or nickname",
            )

        "Check if our server is of multi-type SummonerAndSpectorServerModel, so EUW, EUNE, NA, etc"
        if isinstance(server, SummonerAndSpectorServerModel):
            "Create var that will be used to determine whether we are dealing with a main server (EUROPE, ASIA etc) or minor server (EUW, EUNE, KR)"
            mapped_server = get_mapped_server(server)
        else:
            "If not then check if its either of type AccountModel (without SEA) or MatchModel (without ESPORTS)"
            if isinstance(server, AccountModel):
                pass
            if isinstance(server, MatchModel):
                pass

        if not puuid:
            if "_" in summoner_name:
                summoner_name, tag_line = summoner_name.split("_", 1)
            elif server.value:
                tag_line = server.value

            if mapped_server:
                controller = AccountController(mapped_server)
            else:
                controller = AccountController(server)
            puuid = controller.get_account_by_riot_id(summoner_name, tag_line)

        kwargs.pop("puuid", None)
        kwargs.pop("mapped_server", None)

        return await func(mapped_server=mapped_server, puuid=puuid, *args, **kwargs)

    return wrapper


def map_identity_to_puuid(func: Callable) -> Callable:
    @wraps(func)
    async def wrapper(*args, **kwargs):
        """
        This mapper detects whether provided identity is a nickname or a puuid.
        If identity is a nickname, it tries to get puuid from riot api.
        If identity is a puuid, it simply returns it.
        """
        identity = kwargs.get("identity")
        server = kwargs.get("server")

        if not identity:
            raise HTTPException(
                status_code=500,
                detail="Identity not found in wrapped function",
            )

        "Check if our server is of multi-type SummonerAndSpectorServerModel, so EUW, EUNE, NA, etc"
        if isinstance(server, SummonerAndSpectorServerModel):
            "Create var that will be used to determine whether we are dealing with a main server (EUROPE, ASIA etc) or minor server (EUW, EUNE, KR)"
            mapped_server = get_mapped_server(server)
        else:
            "If not then check if its either of type AccountModel (without SEA) or MatchModel (without ESPORTS)"
            if isinstance(server, AccountModel):
                pass
            if isinstance(server, MatchModel):
                pass

        if len(identity) == 78:
            "The puuid always has 78 characters"
            puuid = identity
        else:
            "Identity is a nickname (or a nickname with a tag) and we have to resolve puuid based on it"
            summoner_name = identity
            if "_" in summoner_name:
                summoner_name, tag_line = summoner_name.split("_", 1)
            elif server.value:
                tag_line = server.value

            if mapped_server:
                controller = AccountController(mapped_server)
            else:
                controller = AccountController(server)
            puuid = controller.get_account_by_riot_id(summoner_name, tag_line)

        kwargs.pop("puuid", None)
        kwargs.pop("mapped_server", None)

        return await func(mapped_server=mapped_server, puuid=puuid, *args, **kwargs)

    return wrapper


def retry_on_429():
    """Decorator that implements retry logic for API requests."""
    max_retries = 3
    wait_time = 120

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except HTTPException as e:
                    if e.status_code == 429:
                        retries += 1
                        if retries < max_retries:
                            logger.warning(
                                f"Rate limit exceeded. Waiting {wait_time} seconds. "
                                f"Retry attempt {retries}/{max_retries}"
                            )
                            time.sleep(wait_time)
                            continue
                    raise
            return func(*args, **kwargs)

        return wrapper

    return decorator


def retry_on_503():
    """Decorator that implements retry logic for API requests.
    503 is usually Riot's fault and service is unavailable for very short period of time, thus low waiting time
    """
    max_retries = 10
    wait_time = 2

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except HTTPException as e:
                    if e.status_code == 503:
                        retries += 1
                        if retries < max_retries:
                            logger.warning(
                                f"Service might be temporarily unavailable. Waiting {wait_time} seconds. "
                                f"Retry attempt {retries}/{max_retries}"
                            )
                            time.sleep(wait_time)
                            continue
                    raise
            return func(*args, **kwargs)

        return wrapper

    return decorator
