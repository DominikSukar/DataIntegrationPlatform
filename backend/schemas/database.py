from enum import Enum
from pydantic import BaseModel, Field


class MatchType(str, Enum):
    _all: str = "all"
    normal: str = "normal"
    ranked: str = "ranked"
    tournament: str = "tournament"


class MatchQueryModel(BaseModel):
    count: int = Field(
        default=10,
        ge=0,
        le=100,
        description="Number of match ids to return. Valid values: 0 to 100.",
    )
    match_type: MatchType = Field(
        default=MatchType.ranked,
        description="Filter the list of match ids by the type of match.",
    )
    resolve_integrity: bool = Field(
        default=False,
        description="Resolve whether server data is up to date with Riot API",
    )
