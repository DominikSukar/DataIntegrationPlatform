from typing import List
from pydantic import BaseModel, Field


class BannedChampion(BaseModel):
    pick_turn: int = Field(..., alias="pickTurn")
    champion_id: int = Field(..., alias="championId")
    team_id: int = Field(..., alias="teamId")


class Observer(BaseModel):
    encryption_key: str = Field(..., alias="encryptionKey")


class Perks(BaseModel):
    perk_ids: List[int] = Field(..., alias="perkIds")
    perk_style: int = Field(..., alias="perkStyle")
    perk_sub_style: int = Field(..., alias="perkSubStyle")


class GameCustomizationObject(BaseModel):
    category: str
    content: str


class CurrentGameParticipant(BaseModel):
    champion_id: int = Field(..., alias="championId")
    perks: Perks
    profile_icon_id: int = Field(..., alias="profileIconId")
    bot: bool
    team_id: int = Field(..., alias="teamId")
    summoner_id: str = Field(..., alias="summonerId")
    puuid: str
    spell1_id: int = Field(..., alias="spell1Id")
    spell2_id: int = Field(..., alias="spell2Id")
    game_customization_objects: List[GameCustomizationObject] = Field(
        ..., alias="gameCustomizationObjects"
    )


class CurrentGameInfo(BaseModel):
    game_id: int = Field(..., alias="gameId")
    game_type: str = Field(..., alias="gameType")
    game_start_time: int = Field(..., alias="gameStartTime")
    map_id: int = Field(..., alias="mapId")
    game_length: int = Field(..., alias="gameLength")
    platform_id: str = Field(..., alias="platformId")
    game_mode: str = Field(..., alias="gameMode")
    banned_champions: List[BannedChampion] = Field(..., alias="bannedChampions")
    game_queue_config_id: int = Field(..., alias="gameQueueConfigId")
    observers: Observer
    participants: List[CurrentGameParticipant] = Field(..., alias="participants")


class Participant(BaseModel):
    bot: bool
    spell2_id: int = Field(..., alias="spell2Id")
    profile_icon_id: int = Field(..., alias="profileIconId")
    summoner_id: str = Field(..., alias="summonerId")
    puuid: str
    champion_id: int = Field(..., alias="championId")
    team_id: int = Field(..., alias="teamId")
    spell1_id: int = Field(..., alias="spell1Id")


class FeaturedGameInfo(BaseModel):
    game_mode: str = Field(..., alias="gameMode")
    game_length: int = Field(..., alias="gameLength")
    map_id: int = Field(..., alias="mapId")
    game_type: str = Field(..., alias="gameType")
    banned_champions: List[BannedChampion] = Field(..., alias="bannedChampions")
    game_id: int = Field(..., alias="gameId")
    observers: Observer
    game_queue_config_id: int = Field(..., alias="gameQueueConfigId")
    participants: List[Participant] = Field(..., alias="participants")
    platform_id: str = Field(..., alias="platformId")


class FeaturedGames(BaseModel):
    game_list: List[FeaturedGameInfo] = Field(..., alias="gameList")
    client_refresh_interval: int = Field(..., alias="clientRefreshInterval")
