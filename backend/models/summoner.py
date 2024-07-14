from pydantic import BaseModel, Field


class SummonerByNickname(BaseModel):
    name: str = Field(..., example="PrinceOfEssling")
    tag: str = Field(..., example="EUW")


class SummonerByPUUID(BaseModel):
    puuuid: str = Field(
        ...,
        example="Bh1lQALIiYypSsY1PGNULQhGCM6hy3ejaLmHiUZXbR84yPOuD7jMa9PhVlwI42mcdpteq-RYWNw-RA",
    )
