import logging
from typing import Any, Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from database.database import get_db
from serializers.basic.summoner_spell import (
    SummonerSpellCreate,
    SummonerSpellResponse,
    SummonerSpellUpdate,
)
from database.models.basic.summoner_spell import SummonerSpell

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/")
async def get_summoner_spells(
    db: Session = Depends(get_db),
    riot_id: Optional[int] = Query(
        None, description="Filter summoner spells by riot_id"
    ),
    name: Optional[str] = Query(None, description="Filter summoner spells by name"),
) -> list[SummonerSpellResponse]:
    summoner_spells = db.query(SummonerSpell).order_by(SummonerSpell.id)

    if riot_id is not None:
        summoner_spells = summoner_spells.filter(SummonerSpell.riot_id == riot_id)

    if name is not None:
        summoner_spells = summoner_spells.filter(SummonerSpell.name.ilike(f"%{name}%"))

    summoner_spells = summoner_spells.all()

    logger.debug(f"Returning data of all summoner spells ({summoner_spells})")

    return summoner_spells


@router.post("/", status_code=201)
async def post_summoner_spell(
    summoner_spell: SummonerSpellCreate, db: Session = Depends(get_db)
) -> SummonerSpellResponse:
    summoner_spell = SummonerSpell(**summoner_spell.model_dump())
    db.add(summoner_spell)
    db.commit()
    db.refresh(summoner_spell)
    logger.info(f"Added new summoner spell ({summoner_spell})")

    return summoner_spell


@router.get("/{summoner_spell_id}")
async def get_summoner_spell(
    summoner_spell_id: int, db: Session = Depends(get_db)
) -> SummonerSpellResponse | Any:
    item = db.get(SummonerSpell, summoner_spell_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    logger.debug(f"Returning data of an summoner spell ({item.name})")

    return item


@router.patch("/{summoner_spell_id}")
async def patch_summoner_spell(
    summoner_spell_id: int,
    summoner_spell_update: SummonerSpellUpdate,
    db: Session = Depends(get_db),
) -> SummonerSpellResponse:
    summoner_spell = db.get(SummonerSpell, summoner_spell_id)
    if not summoner_spell:
        raise HTTPException(status_code=404, detail="Summoner spell not found")

    summoner_spell_data = summoner_spell_update.model_dump(exclude_unset=True)
    for key, value in summoner_spell_data.items():
        setattr(summoner_spell, key, value)

    db.commit()
    db.refresh(summoner_spell)
    logger.info(
        f"Summoner spell ({summoner_spell.name}) has been updated with following data: ({summoner_spell_data})"
    )

    return summoner_spell


@router.delete("/{summoner_spell_id}")
async def delete_summoner_spell(
    summoner_spell_id: int, db: Session = Depends(get_db)
) -> SummonerSpellResponse:
    summoner_spell = db.get(SummonerSpell, summoner_spell_id)
    if not summoner_spell:
        raise HTTPException(status_code=404, detail="Summoner spell not found")

    db.delete(summoner_spell)
    db.commit()
    logger.info(
        f"Summoner spell ({summoner_spell.name}) with id=({summoner_spell_id}) has been deleted."
    )

    return summoner_spell
