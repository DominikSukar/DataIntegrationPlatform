from typing import List

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
from serializers.match.match import MatchParticipantResponse

logger = get_logger(__name__)
router = APIRouter()


@router.get("/matches/{server}/{identity}")
@map_identity_to_puuid
async def get_players_matches_participation(
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
