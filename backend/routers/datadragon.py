import logging
import json

from fastapi import APIRouter, HTTPException

from utils.env import ITEMS_PATH, SUMMONERS_PATH

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/items/")
async def get_items():
    "Fetches data about items"
    try:
        with open(ITEMS_PATH, "r", encoding="utf-8") as file:
            item_data = json.load(file)

        items = {}
        for id, item in item_data["data"].items():
            items[id] = {
                "name": item["name"],
                "description": item["description"],
                "gold": {"total": item["gold"]["total"]},
            }

        return items

    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Item data file not found")

    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Error parsing item data")

    except KeyError as e:
        raise HTTPException(
            status_code=500, detail=f"Unexpected data structure: {str(e)}"
        )


@router.get("/summoners/")
async def get_summoners():
    "Fetches data about summoner spells"
    try:
        with open(SUMMONERS_PATH, "r", encoding="utf-8") as file:
            summoners_data = json.load(file)

        summoners = {}
        for key, summoner in summoners_data["data"].items():
            summoners[summoner["key"]] = {
                "name": summoner["name"],
                "description": summoner["description"],
            }

        return summoners

    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Item data file not found")

    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Error parsing item data")

    except KeyError as e:
        raise HTTPException(
            status_code=500, detail=f"Unexpected data structure: {str(e)}"
        )
