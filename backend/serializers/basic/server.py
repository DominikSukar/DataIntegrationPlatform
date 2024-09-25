from typing import Optional
from pydantic import BaseModel, Field, ConfigDict


class ServerBase(BaseModel):
    full_name: str = Field(..., max_length=50, examples=["Europe Nordic and East"])
    symbol: str = Field(..., max_length=5, examples=["EUNE"])
    riot_symbol: str = Field(..., max_length=5, examples=["EUN1"])
    hostname: str = Field(..., max_length=50, examples=["eun1.api.riotgames.com"])
    active: bool


class ServerCreate(ServerBase):
    pass


class ServerResponse(ServerBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class ServerUpdate(BaseModel):
    full_name: Optional[str] = Field(
        None, max_length=50, examples=["Europe Nordic and East"]
    )
    symbol: Optional[str] = Field(None, max_length=5, examples=["EUNE"])
    riot_symbol: Optional[str] = Field(None, max_length=5, examples=["EUN1"])
    hostname: Optional[str] = Field(
        None, max_length=50, examples=["eun1.api.riotgames.com"]
    )
    active: Optional[bool] = None

    model_config = ConfigDict(from_attributes=True)
