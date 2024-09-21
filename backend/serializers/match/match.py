from pydantic import BaseModel

class MatchBase(BaseModel):
    riot_match_id: str
    game_result: str

class MatchCreate(MatchBase):
    pass

class MatchResponse(MatchBase):
    id: int
    server_id: int

    class Config:
        orm_mode = True