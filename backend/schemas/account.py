from pydantic import BaseModel


class AccountDto(BaseModel):
    puuid: str
    gameName: str
    tagLine: str
