from typing import List, Optional
from pydantic import BaseModel, Field


class AccountDto(BaseModel):
    puuid: str
    gameName: str
    tagLine: str