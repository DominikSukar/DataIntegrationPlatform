from pydantic import BaseModel, ConfigDict


class MatchBase(BaseModel):
    riot_match_id: str
    game_result: str


class MatchCreate(MatchBase):
    pass


class MatchResponse(MatchBase):
    id: int
    server_id: int

    model_coinfig = ConfigDict(from_attributes=True)
