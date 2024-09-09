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
    queueType: str | None = None
    tier: str | None = None
    rank: str | None = None
    leaguePoints: int | None = None
    wins: int | None = None
    losses: int | None = None
    winrate: int | None = None
    hotStreak: bool | None = None
    veteran: bool | None = None
    freshBlood: bool | None = None
    inactive: bool | None = None
