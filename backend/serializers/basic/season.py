from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

from serializers.date_serializers import datetime_serializer


class SeasonBase(BaseModel):
    name: str = Field(..., examples=["S2024"])
    start_date: datetime = Field(
        ...,
        examples=["2024-05-24 00:00:00"],
    )
    end_date: datetime = Field(..., examples=["2024-09-24 23:59:59"])


class SeasonCreate(SeasonBase):
    pass


class SeasonResponse(SeasonBase):
    id: int

    """
    json_encoders are deprecated. Unfortunately there is no good way to solve the serialization
    problem without code duplication. See: https://github.com/pydantic/pydantic/discussions/7199
    """
    model_config = ConfigDict(
        from_attributes=True, json_encoders={datetime: datetime_serializer}
    )


class SeasonUpdate(BaseModel):
    name: Optional[str] = Field(None, examples=["S2024"])
    start_date: Optional[datetime] = Field(
        None,
        examples=["2024-05-24 00:00:00"],
    )
    end_date: Optional[datetime] = Field(None, examples=["2024-09-24 23:59:59"])

    model_config = ConfigDict(from_attributes=True)
