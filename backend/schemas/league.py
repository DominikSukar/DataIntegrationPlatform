from pydantic import BaseModel


class LeagueEntryDTO(BaseModel):
    leagueId: str | None
    summonerId: str | None
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
