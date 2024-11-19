from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from typing import Optional, Annotated, List
from enum import IntEnum

from serializers.basic.perk import MatchParticipantPerk as Perk


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

    perks: List[Perk]

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
                "perks": [
                    {
                        "is_style": False,
                        "match_participant_id": 58,
                        "perk_id": 4,
                        "is_primary": True,
                        "id": 457,
                        "slot": 0,
                        "perk_data": {
                            "riot_id": 9923,
                            "name": "Hail of Blades",
                            "description": "Gain 110% (80% for ranged champions) Attack Speed when you attack an enemy champion for up to 3 attacks.<br><br>No more than 3s can elapse between attacks or this effect will end.<br><br>Cooldown: 12s.<br><br><rules>Attack resets increase the attack limit by 1.<br>Allows you to temporarily exceed the attack speed limit.</rules>",
                        },
                    },
                    {
                        "is_style": False,
                        "match_participant_id": 58,
                        "perk_id": 7,
                        "is_primary": True,
                        "id": 458,
                        "slot": 1,
                        "perk_data": {
                            "riot_id": 8143,
                            "name": "Sudden Impact",
                            "description": "Damaging basic attacks and abilities deal a bonus <trueDamage>20 - 80 True Damage</trueDamage> based on level to enemy champions after using a dash, leap, blink, teleport, or when leaving stealth for 4s.<br><br>Cooldown: 10s",
                        },
                    },
                    {
                        "is_style": False,
                        "match_participant_id": 58,
                        "perk_id": 10,
                        "is_primary": True,
                        "id": 459,
                        "slot": 2,
                        "perk_data": {
                            "riot_id": 8138,
                            "name": "Eyeball Collection",
                            "description": "Collect eyeballs for champion takedowns. Gain an <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Adaptive'><font color='#48C4B7'>adaptive</font></lol-uikit-tooltipped-keyword> bonus of 1.2 Attack Damage or 2 Ability Power, per eyeball collected. <br><br>Upon completing your collection at 10 eyeballs, additionally gain an <lol-uikit-tooltipped-keyword key='LinkTooltip_Description_Adaptive'><font color='#48C4B7'>adaptive</font></lol-uikit-tooltipped-keyword> bonus of 6 Attack Damage, or 10 Ability Power.<br><br>Collect 1 eyeball per champion takedown.",
                        },
                    },
                    {
                        "is_style": False,
                        "match_participant_id": 58,
                        "perk_id": 11,
                        "is_primary": True,
                        "id": 460,
                        "slot": 3,
                        "perk_data": {
                            "riot_id": 8135,
                            "name": "Treasure Hunter",
                            "description": "Gain an additional <gold>50 gold</gold> the next time you collect a <i>Bounty Hunter</i> stack. Increase the gold gained by <gold>20 gold</gold> for each <i>Bounty Hunter</i> stack, up to <gold>130 gold</gold>.<br><br><i>Bounty Hunter</i> stacks are earned the first time you get a takedown on each enemy champion.",
                        },
                    },
                    {
                        "is_style": True,
                        "match_participant_id": 58,
                        "perk_id": 1,
                        "is_primary": True,
                        "id": 461,
                        "slot": 3,
                        "perk_data": {
                            "riot_id": 8100,
                            "name": "Domination",
                            "description": None,
                        },
                    },
                    {
                        "is_style": False,
                        "match_participant_id": 58,
                        "perk_id": 33,
                        "is_primary": False,
                        "id": 462,
                        "slot": 0,
                        "perk_data": {
                            "riot_id": 9111,
                            "name": "Triumph",
                            "description": "Takedowns restore 5% of your missing health, 2.5% of your max health, and grant an additional 20 gold. <br><br><hr><br><i>'The most dangerous game brings the greatest glory.' <br>—Noxian Reckoner</i>",
                        },
                    },
                    {
                        "is_style": False,
                        "match_participant_id": 58,
                        "perk_id": 36,
                        "is_primary": False,
                        "id": 463,
                        "slot": 1,
                        "perk_data": {
                            "riot_id": 9105,
                            "name": "Legend: Haste",
                            "description": "Gain 1.5 basic ability haste for every <i>Legend</i> stack (<statGood>max 10 stacks</statGood>).<br><br>Earn progress toward <i>Legend</i> stacks for every champion takedown, epic monster takedown, large monster kill, and minion kill.",
                        },
                    },
                    {
                        "is_style": True,
                        "match_participant_id": 58,
                        "perk_id": 27,
                        "is_primary": False,
                        "id": 464,
                        "slot": 1,
                        "perk_data": {
                            "riot_id": 8000,
                            "name": "Precision",
                            "description": None,
                        },
                    },
                ],
            }
        }
