from functools import wraps
from fastapi import HTTPException
from typing import Callable

def require_puuid_or_nickname_and_tag(
    func: Callable
) -> Callable:
    @wraps(func)
    async def wrapper(*args, **kwargs):
        # Extract parameters from kwargs
        puuid = kwargs.get('puuid')
        summoner_name = kwargs.get('summoner_name')
        tag_line = kwargs.get('tag_line')

        if (not puuid and not (summoner_name and tag_line)) or ((puuid and tag_line) or (puuid and summoner_name)):
            raise HTTPException(
                status_code=400,
                detail="Please provide either puuid or nickname and tag pair",
            )
        
        if not puuid:
            print("not puuid")
        if not (summoner_name and tag_line):
            print("not s & t")
        print(f"validation passed for {puuid, summoner_name, tag_line} ")
        
        return await func(*args, **kwargs)
    
    return wrapper
