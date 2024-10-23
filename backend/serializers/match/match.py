from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from typing import Optional, Annotated
from enum import IntEnum


class MatchBase(BaseModel):
    riot_match_id: str
    game_result: str
    creation_date: datetime
    end_date: datetime
    game_duration: int
    split_id: int


class MatchCreate(MatchBase):
    pass


class MatchResponse(MatchBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class TeamId(IntEnum):
    BLUE = 100
    RED = 200


class ChampionTransform(IntEnum):
    NONE = 0
    SLAYER = 1
    ASSASSIN = 2


class MatchParticipantResponse(BaseModel):
    """
    Data about a specific player in a match
    """

    id: int
    summoner_id: int
    match_id: int
    match_team_id: int

    team_id: TeamId = Field(description="100 for blue, 200 for red")
    win: bool

    individual_position: str = Field(max_length=20)
    team_position: str = Field(max_length=20)

    champion_id: int
    champion_level: Annotated[int, Field(ge=1, le=18)]
    champion_transform: ChampionTransform = Field(
        description="Kayn's transformation: 0 - None, 1 - Slayer, 2 - Assassin"
    )

    kills: Annotated[int, Field(ge=0)]
    deaths: Annotated[int, Field(ge=0)]
    assists: Annotated[int, Field(ge=0)]
    kda: float = Field(description="Kill/Death/Assist ratio")
    kill_participation: Annotated[
        int,
        Field(ge=0, le=100, description="Percentage of kills participated in times"),
    ]
    total_minions_killed: Annotated[int, Field(ge=0)]
    vision_score: Annotated[int, Field(ge=0)]
    gold_earned: Annotated[int, Field(ge=0)]

    objective_stolen: Annotated[int, Field(ge=0)]
    objective_stolen_assists: Annotated[int, Field(ge=0)]
    turret_kills: Annotated[int, Field(ge=0)]
    turret_takedown: Annotated[int, Field(ge=0)]

    damage_to_champions: Annotated[int, Field(ge=0)]
    damage_to_turrets: Annotated[int, Field(ge=0)]
    damage_self_mitigated: Annotated[int, Field(ge=0)]
    damage_taken: Annotated[int, Field(ge=0)]

    damage_shielded_to_champions: Annotated[int, Field(ge=0)]
    total_heals_on_teammates: Annotated[int, Field(ge=0)]

    item_0: Optional[int] = None
    item_1: Optional[int] = None
    item_2: Optional[int] = None
    item_3: Optional[int] = None
    item_4: Optional[int] = None
    item_5: Optional[int] = None
    item_6: Optional[int] = None

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "summoner_id": 123,
                "match_id": 456,
                "match_team_id": 789,
                "team_id": 100,
                "win": True,
                "individual_position": "MIDDLE",
                "team_position": "MIDDLE",
                "champion_id": 1,
                "champion_level": 18,
                "champion_transform": 0,
                "kills": 5,
                "deaths": 2,
                "assists": 10,
                "kda": 7.5,
                "kill_participation": 65,
                "total_minions_killed": 200,
                "vision_score": 25,
                "gold_earned": 14500,
                "objective_stolen": 0,
                "objective_stolen_assists": 1,
                "turret_kills": 2,
                "turret_takedown": 3,
                "damage_to_champions": 25000,
                "damage_to_objectives": 5000,
                "damage_to_turrets": 3000,
                "damage_self_mitigated": 15000,
                "damage_taken": 20000,
                "damage_shielded_to_champions": 1000,
                "total_heals_on_teammates": 500,
                "item_0": 3157,
                "item_1": 3089,
                "item_2": 3135,
                "item_3": 3158,
                "item_4": 3363,
                "item_5": 3364,
                "item_6": 3340,
            }
        }
