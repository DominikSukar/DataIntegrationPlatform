from typing import List, Optional
from pydantic import BaseModel, Field


class SummonerDTO(BaseModel):
    accountId: str
    profileIconId: int
    revisionDate: float
    id: str
    puuid: str
    summonerLevel: float
