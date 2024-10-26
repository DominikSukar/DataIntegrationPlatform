from typing import Optional, List

from fastapi import APIRouter, Query, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from logger import get_logger
from database.database import get_db
from database.models.match.match import Match
from serializers.match.match import MatchParticipantResponse

logger = get_logger(__name__)
router = APIRouter()


@router.get("/")
async def get_matches(
    db: Session = Depends(get_db),
    riot_match_id: Optional[str] = Query(
        None, description="Filter matches by riot_match_id"
    ),
    split_id: Optional[str] = Query(None, description="Filter matches by split_id"),
) -> List[MatchParticipantResponse]:
    "Endpoint fetches all matches from database"

    matches = db.query(Match).order_by(Match.id)

    if riot_match_id is not None:
        matches = matches.filter(Match.riot_match_id == riot_match_id)

    if split_id is not None:
        matches = matches.filter(Match.split_id == split_id)

    matches = matches.all()

    return matches


@router.get("/{match_id}")
async def get_match(
    match_id: str, db: Session = Depends(get_db)
) -> MatchParticipantResponse:
    "Endpoint fetches specific match from database"

    match = db.execute(select(Match).filter(Match.id == match_id)).scalars().all()

    return match
