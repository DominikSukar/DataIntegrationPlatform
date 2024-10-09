from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

from serializers.date_serializers import datetime_serializer


class SplitBase(BaseModel):
    name: str = Field(..., examples=["S1"])
    season_id: int = Field(..., examples=[1])
    start_date: datetime = Field(
        ...,
        examples=["2024-05-24 00:00:00"],
    )
    end_date: datetime = Field(..., examples=["2024-09-24 23:59:59"])


class SplitCreate(SplitBase):
    pass


class SplitResponse(SplitBase):
    id: int

    """
    json_encoders are deprecated. Unfortunately there is no good way to solve the serialization
    problem without code duplication. See: https://github.com/pydantic/pydantic/discussions/7199
    """
    model_config = ConfigDict(
        from_attributes=True, json_encoders={datetime: datetime_serializer}
    )


class SplitUpdate(BaseModel):
    name: Optional[str] = Field(None, examples=["S1"])
    season_id: Optional[int] = Field(None, examples=[1])
    start_date: Optional[datetime] = Field(
        None,
        examples=["2024-05-24 00:00:00"],
    )
    end_date: Optional[datetime] = Field(None, examples=["2024-09-24 23:59:59"])

    model_config = ConfigDict(from_attributes=True)
