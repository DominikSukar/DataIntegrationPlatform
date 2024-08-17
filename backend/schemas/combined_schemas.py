from pydantic import BaseModel


class LeagueAndSummonerEntryDTO(BaseModel):
    accountId: str
    profileIconId: int
    revisionDate: float
    id: str
    puuid: str
    summonerLevel: float
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
