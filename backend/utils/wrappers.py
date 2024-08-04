from functools import wraps
from fastapi import HTTPException
from typing import Callable
from enum import Enum

from models import AccountModel, MatchModel, SummonerAndSpectorServerModel
from api_requests.account import AccountController
from utils.domain_routers import get_mapped_server

def map_server(
    func: Callable
) -> Callable:
    @wraps(func)
    async def wrapper(*args, **kwargs):
        server = kwargs.get('server')        
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

        kwargs.pop('mapped_server', None) 
        
        return await func(mapped_server=mapped_server, *args, **kwargs)
    
    return wrapper

def map_puuid_and_server(
    func: Callable
) -> Callable:
    @wraps(func)
    async def wrapper(*args, **kwargs):
        # Extract parameters from kwargs
        puuid = kwargs.get('puuid')
        summoner_name = kwargs.get('summoner_name')
        server = kwargs.get('server')

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

        kwargs.pop('puuid', None)
        kwargs.pop('mapped_server', None) 
        
        return await func(mapped_server=mapped_server, puuid=puuid, *args, **kwargs)
    
    return wrapper
