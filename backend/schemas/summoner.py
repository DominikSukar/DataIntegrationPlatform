from pydantic import BaseModel


class SummonerDTO(BaseModel):
    accountId: str
    profileIconId: int
    revisionDate: float
    id: str
    puuid: str
    summonerLevel: float
