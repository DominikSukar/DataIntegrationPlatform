from typing import Optional
from pydantic import BaseModel, Field, ConfigDict


class SummonerSpellBase(BaseModel):
    riot_id: int = Field(..., examples=[21])
    name: str = Field(..., max_length=20, examples=["Barrier"])
    description: str = Field(
        ...,
        examples=["Gain a 120-480 damage Shield for 2.5 seconds."],
    )


class SummonerSpellCreate(SummonerSpellBase):
    pass


class SummonerSpellResponse(SummonerSpellBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class SummonerSpellUpdate(BaseModel):
    riot_id: Optional[int] = Field(None, examples=[21])
    name: Optional[str] = Field(None, max_length=20, examples=["Barrier"])
    description: Optional[str] = Field(
        None,
        examples=["Gain a 120-480 damage Shield for 2.5 seconds."],
    )

    model_config = ConfigDict(from_attributes=True)
