from pydantic import BaseModel


class LeagueEntryDTO(BaseModel):
    leagueId: str
    summonerId: str
    queueType: str
    tier: str
    rank: str
    leaguePoints: int
    wins: int
    losses: int
    hotStreak: bool
    veteran: bool
    freshBlood: bool
    inactive: bool
