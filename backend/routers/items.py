import logging
from typing import Any, Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from database.database import get_db
from serializers.basic.item import ItemResponse, ItemCreate, ItemUpdate
from database.models.basic.item import Item

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/")
async def get_items(
    db: Session = Depends(get_db),
    riot_id: Optional[int] = Query(None, description="Filter items by riot_id"),
    name: Optional[str] = Query(None, description="Filter items by name"),
) -> list[ItemResponse]:
    items = db.query(Item).order_by(Item.id)

    if riot_id is not None:
        items = items.filter(Item.riot_id == riot_id)

    if name is not None:
        items = items.filter(Item.name.ilike(f"%{name}%"))

    items = items.all()

    logger.debug(f"Returning data of all items ({items})")

    return items


@router.post("/", status_code=201)
async def post_item(item: ItemCreate, db: Session = Depends(get_db)) -> ItemResponse:
    new_item = Item(**item.model_dump())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    logger.info(f"Added new item ({new_item})")

    return new_item


@router.get("/{item_id}")
async def get_item(item_id: int, db: Session = Depends(get_db)) -> ItemResponse | Any:
    item = db.get(Item, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    logger.debug(f"Returning data of an item ({item.name})")

    return item


@router.patch("/{item_id}")
async def patch_item(
    item_id: int, item_update: ItemUpdate, db: Session = Depends(get_db)
) -> ItemResponse:
    item = db.get(Item, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    item_data = item_update.model_dump(exclude_unset=True)
    for key, value in item_data.items():
        setattr(item, key, value)

    db.commit()
    db.refresh(item)
    logger.info(
        f"Item ({item.name}) has been updated with following data: ({item_data})"
    )

    return item


@router.delete("/{item_id}")
async def delete_item(item_id: int, db: Session = Depends(get_db)) -> ItemResponse:
    item = db.get(Item, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    db.delete(item)
    db.commit()
    logger.info(f"Item ({item.name}) with id=({item_id}) has been deleted.")

    return item
