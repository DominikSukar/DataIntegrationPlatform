import requests
import logging
import json

from fastapi import HTTPException

logger = logging.getLogger(__name__)

def send_request(URL: str):
    """This function in supposed to be used by all requests to RIOT API"""
    response = requests.get(URL)
    status_code = response.status_code

    if status_code in [400, 401, 403, 405, 415, 429, 500, 502, 503, 504]:
        logger.error(
            f"Error: {response.status_code}:{response.text}. URL: {URL}"
        )
        raise HTTPException(
            status_code=503, detail="Failed to retrieve data from Riot's API"
        )
    elif status_code in [404]:
        raise HTTPException(
            status_code=status_code, detail="Data not found"
        )

    data = json.loads(response.text)

    return data       