import requests
import logging
import json

from fastapi import HTTPException

logger = logging.getLogger(__name__)


def _handle_non_200(response, URL=None):
    status_code = response.status_code

    if status_code in [401, 403, 405, 415, 429, 500, 502, 503, 504]:
        logger.error(f"Error: {response.status_code}:{response.text}. URL: {URL}")
        raise HTTPException(
            status_code=503, detail="Failed to retrieve data from Riot's API"
        )

    elif status_code in [400]:
        logger.error(f"Error: {response.status_code}:{response.text}. URL: {URL}")
        raise HTTPException(status_code=status_code, detail=response.text)

    elif status_code in [404]:
        raise HTTPException(status_code=status_code, detail="Data not found")
    else:
        raise HTTPException(status_code=status_code, detail="Unspecified error")


def send_request(URL: str):
    """This function in supposed to be used by all requests to RIOT API"""
    response = requests.get(URL)

    if response.status_code == 200:
        data = json.loads(response.text)
        return data
    else:
        _handle_non_200(response, URL)


async def send_async_request(session, URL: str):
    """This function in supposed to be used by all requests to RIOT API"""

    async with session.get(URL) as response:
        if response.status == 200:
            return await response.json()
        else:
            _handle_non_200(response, URL)
