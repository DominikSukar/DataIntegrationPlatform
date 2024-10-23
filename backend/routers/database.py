from typing import Optional, List

from logger import get_logger

from fastapi import APIRouter, Query, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from schemas import MatchModel, SummonerAndSpectorServerModel, MatchQueryModel
from utils.wrappers.mappers import map_identity_to_puuid
from database.database import get_db
from routers_services.database.matches_num_in_dbs import (
    resolve_data_intergrity,
    get_summoner_id,
)
from database.models.match.match_participant import MatchParticipant
from database.models.match.match import Match
from serializers.match.match import MatchParticipantResponse

logger = get_logger(__name__)
router = APIRouter()


@router.get("/matches/{server}/{identity}")
@map_identity_to_puuid
async def get_players_matches(
    server: SummonerAndSpectorServerModel,
    identity: str,
    summoner_name: str = Query(None, include_in_schema=False),
    puuid: str = Query(None, include_in_schema=False),
    mapped_server: MatchModel = Query(None, include_in_schema=False),
    query_params: MatchQueryModel = Depends(),
    db: Session = Depends(get_db),
) -> List[MatchParticipantResponse]:
    """Fetches data with last games requested summoner participated in"""

    # Resolves whether server data is up to date with Riot API
    if query_params.resolve_integrity:
        await resolve_data_intergrity(
            server=server,
            mapped_server=mapped_server,
            puuid=puuid,
            match_type=query_params.match_type,
            db=db,
        )
    (summoner, _) = await get_summoner_id(server, db, puuid)
    matches = (
        db.execute(
            select(MatchParticipant)
            .filter(MatchParticipant.summoner_id == summoner.id)
            .limit(query_params.count)
        )
        .scalars()
        .all()
    )

    return matches


@router.get("/matches/{match_id}")
async def get_match(
    match_id: str, db: Session = Depends(get_db)
) -> MatchParticipantResponse:
    "Endpoint fetches specific match from database"

    match = db.execute(select(Match).filter(Match.id == match_id)).scalars().all()

    return match


@router.get("/matches/")
async def get_matches(
    db: Session = Depends(get_db),
    riot_match_id: Optional[str] = Query(
        None, description="Filter matches by riot_match_id"
    ),
    split_id: Optional[str] = Query(None, description="Filter matches by split_id"),
):
    "Endpoint fetches all matches from database"

    matches = db.query(Match).order_by(Match.id)

    if riot_match_id is not None:
        matches = matches.filter(Match.riot_match_id == riot_match_id)

    if split_id is not None:
        matches = matches.filter(Match.split_id == split_id)

    matches = matches.all()

    return matches
