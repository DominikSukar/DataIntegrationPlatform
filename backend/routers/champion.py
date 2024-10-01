import logging
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.database import get_db
from serializers.basic.champion import ChampionCreate, ChampionResponse, ChampionUpdate
from database.models.basic.champion import Champion

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/")
async def get_champions(db: Session = Depends(get_db)) -> list[ChampionResponse]:
    champions = db.query(Champion).order_by(Champion.id).all()
    logger.debug(f"Returning data of all champions ({champions})")

    return champions


@router.post("/", status_code=201)
async def post_champion(
    server: ChampionCreate, db: Session = Depends(get_db)
) -> ChampionResponse:
    new_champion = Champion(**server.model_dump())
    db.add(new_champion)
    db.commit()
    db.refresh(new_champion)
    logger.info(f"Added new champion ({new_champion})")

    return new_champion


@router.get("/{champion_id}")
async def get_champion(
    champion_id: int, db: Session = Depends(get_db)
) -> ChampionResponse | Any:
    champion = db.get(Champion, champion_id)
    if not champion:
        raise HTTPException(status_code=404, detail="Champion not found")
    logger.debug(f"Returning data of a champion ({champion.name})")

    return champion


@router.patch("/{champion_id}")
async def patch_champion(
    champion_id: int, champion_update: ChampionUpdate, db: Session = Depends(get_db)
) -> ChampionResponse:
    champion = db.get(Champion, champion_id)
    if not champion:
        raise HTTPException(status_code=404, detail="Item not found")

    champion_data = champion_update.model_dump(exclude_unset=True)
    for key, value in champion_data.items():
        setattr(champion, key, value)

    db.commit()
    db.refresh(champion)
    logger.info(
        f"Champion ({champion.name}) has been updated with following data: ({champion_data})"
    )

    return champion


@router.delete("/{champion_id}")
async def delete_item(
    champion_id: int, db: Session = Depends(get_db)
) -> ChampionResponse:
    champion = db.get(Champion, champion_id)
    if not champion:
        raise HTTPException(status_code=404, detail="Item not found")

    db.delete(champion)
    db.commit()
    logger.info(f"Champion ({champion.name}) with id=({champion_id}) has been deleted.")

    return champion
