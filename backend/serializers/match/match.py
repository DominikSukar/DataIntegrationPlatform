from datetime import datetime
from pydantic import BaseModel, ConfigDict


class MatchBase(BaseModel):
    riot_match_id: str
    game_result: str
    creation_date: datetime
    end_date: datetime
    game_duration: int
    split_id: int


class MatchCreate(MatchBase):
    pass


class MatchResponse(MatchBase):
    id: int

    model_coinfig = ConfigDict(from_attributes=True)
