from typing import Optional
from pydantic import BaseModel, Field, ConfigDict


class PerkBase(BaseModel):
    riot_id: int = Field(..., examples=[8112])
    name: str = Field(..., max_length=20, examples=["Electrocute"])
    description: str = Field(
        ...,
        examples=[
            "Hitting a champion with 3 <b>separate</b> attacks or abilities within 3s deals bonus <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_AdaptiveDmg'><font color='#48C4B7'>adaptive damage</font></lol-uikit-tooltipped-keyword>.<br><br>Damage: 50 - 190 (+0.1 bonus AD, +0.05 AP) damage.<br><br>Cooldown: 20s<br><br><hr><i>'We called them the Thunderlords, for to speak of their lightning was to invite disaster.'</i>"
        ],
    )


class PerkCreate(PerkBase):
    pass


class PerkResponse(PerkBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class PerkUpdate(BaseModel):
    riot_id: Optional[int] = Field(None, examples=[8112])
    name: Optional[str] = Field(None, max_length=20, examples=["Electrocute"])
    description: Optional[str] = Field(
        None,
        examples=[
            "Hitting a champion with 3 <b>separate</b> attacks or abilities within 3s deals bonus <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_AdaptiveDmg'><font color='#48C4B7'>adaptive damage</font></lol-uikit-tooltipped-keyword>.<br><br>Damage: 50 - 190 (+0.1 bonus AD, +0.05 AP) damage.<br><br>Cooldown: 20s<br><br><hr><i>'We called them the Thunderlords, for to speak of their lightning was to invite disaster.'</i>"
        ],
    )

    model_config = ConfigDict(from_attributes=True)
