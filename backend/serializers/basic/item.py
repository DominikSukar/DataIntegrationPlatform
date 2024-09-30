from typing import Optional
from pydantic import BaseModel, Field, ConfigDict


class ItemBase(BaseModel):
    riot_id: int = Field(..., examples=[1001])
    name: str = Field(..., max_length=20, examples=["Boots"])
    description: str = Field(
        ...,
        examples=[
            "<mainText><stats><attention>25</attention> Move Speed</stats><br><br></mainText>"
        ],
    )
    cost: int = Field(..., ge=0, le=32767, examples=[300])


class ItemCreate(ItemBase):
    pass


class ItemResponse(ItemBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class ItemUpdate(BaseModel):
    riot_id: Optional[int] = Field(None, examples=[1001])
    name: Optional[str] = Field(None, max_length=20, examples=["Boots"])
    description: Optional[str] = Field(
        None,
        examples=[
            "<mainText><stats><attention>25</attention> Move Speed</stats><br><br></mainText>"
        ],
    )
    cost: Optional[int] = Field(None, ge=0, le=32767, examples=[300])

    model_config = ConfigDict(from_attributes=True)
