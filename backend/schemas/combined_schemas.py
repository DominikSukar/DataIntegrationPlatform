from pydantic import BaseModel


class LeagueAndSummonerEntryDTO(BaseModel):
    accountId: str
    profileIconId: int
    revisionDate: float
    id: str
    puuid: str
    summonerLevel: float
    leagueId: str | None = None
    summonerId: str | None = None
    queueType: str
    tier: str
    rank: str | None = None
    leaguePoints: int
    wins: int
    losses: int
    winrate: int
    hotStreak: bool
    veteran: bool
    freshBlood: bool
    inactive: bool
