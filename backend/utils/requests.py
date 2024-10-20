import requests
import json
from fastapi import HTTPException

from logger import get_logger
from utils.wrappers import retry_on_429, retry_on_503

logger = get_logger(__name__)


def _handle_non_200(status_code, URL=None):
    if status_code == 429:
        logger.warning(f"Rate limit exceeded for URL: {URL}")
        raise HTTPException(status_code=429, detail="Rate limit exceeded")
    elif status_code == 503:
        logger.warning(f"Service might be temporarily unavailable for URL: {URL}")
        raise HTTPException(status_code=503, detail="Service Unavailable")
    elif status_code in [401, 403, 405, 415, 500, 502, 504]:
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


@retry_on_429()
@retry_on_503()
def send_request(URL: str):
    """This function in supposed to be used by all requests to RIOT API"""
    logger.debug(f"Sending synchronous request to : {URL}")
    response = requests.get(URL, verify=False)

    if response.status_code == 200:
        data = json.loads(response.text)
        return data
    else:
        _handle_non_200(response.status_code, URL)


@retry_on_429()
@retry_on_503()
async def send_async_request(session, URL: str):
    """This function in supposed to be used by all requests to RIOT API"""
    logger.debug(f"Sending asynchronous request to : {URL}")

    async with session.get(URL, ssl=False) as response:
        if response.status == 200:
            return await response.json()
        else:
            _handle_non_200(response.status, URL)
