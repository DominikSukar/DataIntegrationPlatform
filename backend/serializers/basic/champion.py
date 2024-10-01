from typing import Optional
from pydantic import BaseModel, Field, ConfigDict


class ChampionBase(BaseModel):
    riot_id: int = Field(..., examples=[266])
    name: str = Field(..., max_length=20, examples=["Aatrox"])


class ChampionCreate(ChampionBase):
    pass


class ChampionResponse(ChampionBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class ChampionUpdate(BaseModel):
    riot_id: Optional[int] = Field(None, examples=[266])
    name: Optional[str] = Field(None, max_length=20, examples=["Aatrox"])

    model_config = ConfigDict(from_attributes=True)
