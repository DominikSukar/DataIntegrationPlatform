import logging
from typing import Any, Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from database.database import get_db
from serializers.basic.perk import PerkResponse, PerkCreate, PerkUpdate
from database.models.basic.perk import Perk

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/")
async def get_perks(
    db: Session = Depends(get_db),
    riot_id: Optional[int] = Query(None, description="Filter perks by riot_id"),
    name: Optional[str] = Query(None, description="Filter perks by name"),
) -> list[PerkResponse]:
    perks = db.query(Perk).order_by(Perk.id)

    if riot_id is not None:
        perks = perks.filter(Perk.riot_id == riot_id)

    if name is not None:
        perks = perks.filter(Perk.name.ilike(f"%{name}%"))

    perks = perks.all()
    logger.debug(f"Returning data of all perks ({perks})")

    return perks


@router.post("/", status_code=201)
async def post_perks(perk: PerkCreate, db: Session = Depends(get_db)) -> PerkResponse:
    new_perk = Perk(**perk.model_dump())
    db.add(new_perk)
    db.commit()
    db.refresh(new_perk)
    logger.info(f"Added new perk ({new_perk})")

    return new_perk


@router.get("/{perk_id}")
async def get_perk(perk_id: int, db: Session = Depends(get_db)) -> PerkResponse | Any:
    perk = db.get(Perk, perk_id)
    if not perk:
        raise HTTPException(status_code=404, detail="Perk not found")
    logger.debug(f"Returning data of an perk ({perk.name})")

    return perk


@router.patch("/{perk_id}")
async def patch_perk(
    perk_id: int, item_update: PerkUpdate, db: Session = Depends(get_db)
) -> PerkResponse:
    perk = db.get(Perk, perk_id)
    if not perk:
        raise HTTPException(status_code=404, detail="Perk not found")

    item_data = item_update.model_dump(exclude_unset=True)
    for key, value in item_data.items():
        setattr(perk, key, value)

    db.commit()
    db.refresh(perk)
    logger.info(
        f"Perk ({perk.name}) has been updated with following data: ({item_data})"
    )

    return perk


@router.delete("/{perk_id}")
async def delete_perk(perk_id: int, db: Session = Depends(get_db)) -> PerkResponse:
    item = db.get(Perk, perk_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    db.delete(item)
    db.commit()
    logger.info(f"Perk ({item.name}) with id=({perk_id}) has been deleted.")

    return item
