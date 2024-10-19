from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from logger import get_logger
from database.database import get_db
from serializers.basic.season import SeasonResponse, SeasonCreate, SeasonUpdate
from database.models.basic.season import Season

logger = get_logger(__name__)
router = APIRouter()


@router.get("/")
async def get_seasons(db: Session = Depends(get_db)) -> list[SeasonResponse]:
    seasons = db.query(Season).order_by(Season.id).all()
    logger.debug(f"Returning data of all seasons ({seasons})")

    return seasons


@router.post("/", status_code=201)
async def post_season(
    season: SeasonCreate, db: Session = Depends(get_db)
) -> SeasonResponse:
    new_season = Season(**season.model_dump())
    db.add(new_season)
    db.commit()
    db.refresh(new_season)
    logger.info(f"Added new season ({new_season})")

    return new_season


@router.get("/{season_id}")
async def get_season(
    season_id: int, db: Session = Depends(get_db)
) -> SeasonResponse | Any:
    season = db.get(Season, season_id)
    if not season:
        raise HTTPException(status_code=404, detail="Season not found")
    logger.debug(f"Returning data of an season ({season.name})")

    return season


@router.patch("/{season_id}")
async def patch_season(
    season_id: int, season_update: SeasonUpdate, db: Session = Depends(get_db)
) -> SeasonResponse:
    season = db.get(Season, season_id)
    if not season:
        raise HTTPException(status_code=404, detail="Season not found")

    season_data = season_update.model_dump(exclude_unset=True)
    for key, value in season_data.items():
        setattr(season, key, value)

    db.commit()
    db.refresh(season)
    logger.info(
        f"Season ({season.name}) has been updated with following data: ({season_data})"
    )

    return season


@router.delete("/{season_id}")
async def delete_season(
    season_id: int, db: Session = Depends(get_db)
) -> SeasonResponse:
    season = db.get(Season, season_id)
    if not season:
        raise HTTPException(status_code=404, detail="Season not found")

    db.delete(season)
    db.commit()
    logger.info(f"Season ({season.name}) with id=({season_id}) has been deleted.")

    return season
