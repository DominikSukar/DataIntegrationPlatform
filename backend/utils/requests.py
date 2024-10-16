import requests
import logging
import json

from fastapi import HTTPException

logger = logging.getLogger(__name__)


def _handle_non_200(status_code, URL=None):

    if status_code in [401, 403, 405, 415, 429, 500, 502, 503, 504]:
        logger.error(f"Error: {status_code} URL: {URL}")
        raise HTTPException(
            status_code=503, detail="Failed to retrieve data from Riot's API"
        )

    elif status_code in [400]:
        logger.error(f"Error: {status_code} URL: {URL}")
        raise HTTPException(status_code=status_code, detail="Client data error")

    elif status_code in [404]:
        raise HTTPException(status_code=status_code, detail="Data not found")
    else:
        raise HTTPException(status_code=status_code, detail="Unspecified error")


def send_request(URL: str):
    """This function in supposed to be used by all requests to RIOT API"""
    logger.debug(f"Sending synchronous request to : {URL}")
    response = requests.get(URL, verify=False)

    if response.status_code == 200:
        data = json.loads(response.text)
        return data
    else:
        _handle_non_200(response.status_code, URL)


async def send_async_request(session, URL: str):
    """This function in supposed to be used by all requests to RIOT API"""
    logger.debug(f"Sending asynchronous request to : {URL}")

    async with session.get(URL, ssl=False) as response:
        if response.status == 200:
            return await response.json()
        else:
            _handle_non_200(response.status, URL)
