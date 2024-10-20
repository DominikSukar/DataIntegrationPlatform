from functools import wraps
from fastapi import HTTPException
import time

from logger import get_logger

logger = get_logger(__name__)


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
