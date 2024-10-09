import logging
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.database import get_db
from serializers.basic.split import SplitResponse, SplitCreate, SplitUpdate
from database.models.basic.split import Split

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/")
async def get_splits(db: Session = Depends(get_db)) -> list[SplitResponse]:
    splits = db.query(Split).order_by(Split.id).all()
    logger.debug(f"Returning data of all splits ({splits})")

    return splits


@router.post("/", status_code=201)
async def post_split(
    split: SplitCreate, db: Session = Depends(get_db)
) -> SplitResponse:
    new_split = Split(**split.model_dump())
    db.add(new_split)
    db.commit()
    db.refresh(new_split)
    logger.info(f"Added new split ({new_split})")

    return new_split


@router.get("/{split_id}")
async def get_split(
    split_id: int, db: Session = Depends(get_db)
) -> SplitResponse | Any:
    split = db.get(Split, split_id)
    if not split:
        raise HTTPException(status_code=404, detail="Split not found")
    logger.debug(f"Returning data of an split ({split.name})")

    return split


@router.patch("/{split_id}")
async def patch_split(
    split_id: int, season_update: SplitUpdate, db: Session = Depends(get_db)
) -> SplitResponse:
    split = db.get(Split, split_id)
    if not split:
        raise HTTPException(status_code=404, detail="Split not found")

    split_data = season_update.model_dump(exclude_unset=True)
    for key, value in split_data.items():
        setattr(split, key, value)

    db.commit()
    db.refresh(split)
    logger.info(
        f"Split ({split.name}) has been updated with following data: ({split_data})"
    )

    return split


@router.delete("/{split_id}")
async def delete_split(split_id: int, db: Session = Depends(get_db)) -> SplitResponse:
    split = db.get(Split, split_id)
    if not split:
        raise HTTPException(status_code=404, detail="Split not found")

    db.delete(split)
    db.commit()
    logger.info(f"Split ({split.name}) with id=({split_id}) has been deleted.")

    return split
