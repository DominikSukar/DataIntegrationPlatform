from typing import List, Optional, Dict
from pydantic import BaseModel, RootModel
from enum import Enum


class MatchIds(RootModel):
    root: List[str]


class MetadataDto(BaseModel):
    dataVersion: str
    matchId: str
    participants: List[str]


class Observer(BaseModel):
    encryptionKey: str


class BanDto(BaseModel):
    championId: int
    pickTurn: int


class ObjectiveDto(BaseModel):
    first: bool
    kills: int


class ObjectivesDto(BaseModel):
    baron: ObjectiveDto
    champion: ObjectiveDto
    dragon: ObjectiveDto
    horde: ObjectiveDto
    inhibitor: ObjectiveDto
    riftHerald: ObjectiveDto
    tower: ObjectiveDto


class PerkStyleSelectionDto(BaseModel):
    perk: int
    var1: int
    var2: int
    var3: int


class PerkStyleDto(BaseModel):
    description: str
    selections: List[PerkStyleSelectionDto]
    style: int


class PerkStatsDto(BaseModel):
    defense: int
    flex: int
    offense: int


class PerksDto(BaseModel):
    statPerks: PerkStatsDto
    styles: List[PerkStyleDto]


class ParticipantDto(BaseModel):
    allInPings: Optional[int]
    assistMePings: Optional[int]
    assists: Optional[int]
    baronKills: Optional[int]
    bountyLevel: Optional[int]
    champExperience: Optional[int]
    champLevel: Optional[int]
    championId: int
    championName: str
    commandPings: Optional[int]
    championTransform: Optional[int]
    consumablesPurchased: Optional[int]
    challenges: Optional["ChallengesDto"]
    damageDealtToBuildings: Optional[int]
    damageDealtToObjectives: Optional[int]
    damageDealtToTurrets: Optional[int]
    damageSelfMitigated: Optional[int]
    deaths: Optional[int]
    detectorWardsPlaced: Optional[int]
    doubleKills: Optional[int]
    dragonKills: Optional[int]
    eligibleForProgression: Optional[bool]
    enemyMissingPings: Optional[int]
    enemyVisionPings: Optional[int]
    firstBloodAssist: Optional[bool]
    firstBloodKill: Optional[bool]
    firstTowerAssist: Optional[bool]
    firstTowerKill: Optional[bool]
    gameEndedInEarlySurrender: Optional[bool]
    gameEndedInSurrender: Optional[bool]
    holdPings: Optional[int]
    getBackPings: Optional[int]
    goldEarned: Optional[int]
    goldSpent: Optional[int]
    individualPosition: Optional[str]
    inhibitorKills: Optional[int]
    inhibitorTakedowns: Optional[int]
    inhibitorsLost: Optional[int]
    item0: Optional[int]
    item1: Optional[int]
    item2: Optional[int]
    item3: Optional[int]
    item4: Optional[int]
    item5: Optional[int]
    item6: Optional[int]
    itemsPurchased: Optional[int]
    killingSprees: Optional[int]
    kills: Optional[int]
    lane: Optional[str]
    largestCriticalStrike: Optional[int]
    largestKillingSpree: Optional[int]
    largestMultiKill: Optional[int]
    longestTimeSpentLiving: Optional[int]
    magicDamageDealt: Optional[int]
    magicDamageDealtToChampions: Optional[int]
    magicDamageTaken: Optional[int]
    missions: Optional["MissionsDto"]
    neutralMinionsKilled: Optional[int]
    needVisionPings: Optional[int]
    nexusKills: Optional[int]
    nexusTakedowns: Optional[int]
    nexusLost: Optional[int]
    objectivesStolen: Optional[int]
    objectivesStolenAssists: Optional[int]
    onMyWayPings: Optional[int]
    participantId: int
    playerScore0: Optional[int]
    playerScore1: Optional[int]
    playerScore2: Optional[int]
    playerScore3: Optional[int]
    playerScore4: Optional[int]
    playerScore5: Optional[int]
    playerScore6: Optional[int]
    playerScore7: Optional[int]
    playerScore8: Optional[int]
    playerScore9: Optional[int]
    playerScore10: Optional[int]
    playerScore11: Optional[int]
    pentaKills: Optional[int]
    perks: Optional[PerksDto]
    physicalDamageDealt: Optional[int]
    physicalDamageDealtToChampions: Optional[int]
    physicalDamageTaken: Optional[int]
    placement: Optional[int]
    playerAugment1: Optional[int]
    playerAugment2: Optional[int]
    playerAugment3: Optional[int]
    playerAugment4: Optional[int]
    playerSubteamId: Optional[int]
    pushPings: Optional[int]
    profileIcon: Optional[int]
    quadraKills: Optional[int]
    riotIdGameName: Optional[str]
    riotIdName: Optional[str]
    riotIdTagline: Optional[str]
    role: Optional[str]
    sightWardsBoughtInGame: Optional[int]
    spell1Casts: Optional[int]
    spell2Casts: Optional[int]
    spell3Casts: Optional[int]
    spell4Casts: Optional[int]
    subteamPlacement: Optional[int]
    summoner1Casts: Optional[int]
    summoner1Id: Optional[int]
    summoner2Casts: Optional[int]
    summoner2Id: Optional[int]
    summonerId: str
    summonerLevel: Optional[int]
    summonerName: Optional[str]
    teamEarlySurrendered: Optional[bool]
    teamId: int
    teamPosition: Optional[str]
    timeCCingOthers: Optional[int]
    timePlayed: Optional[int]
    totalAllyJungleMinionsKilled: Optional[int]
    totalDamageDealt: Optional[int]
    totalDamageDealtToChampions: Optional[int]
    totalDamageShieldedOnTeammates: Optional[int]
    totalDamageTaken: Optional[int]
    totalEnemyJungleMinionsKilled: Optional[int]
    totalHeal: Optional[int]
    totalHealsOnTeammates: Optional[int]
    totalMinionsKilled: Optional[int]
    totalTimeCCDealt: Optional[int]
    totalTimeSpentDead: Optional[int]
    totalUnitsHealed: Optional[int]
    tripleKills: Optional[int]
    trueDamageDealt: Optional[int]
    trueDamageDealtToChampions: Optional[int]
    trueDamageTaken: Optional[int]
    turretKills: Optional[int]
    turretTakedowns: Optional[int]
    turretsLost: Optional[int]
    unrealKills: Optional[int]
    visionScore: Optional[int]
    visionClearedPings: Optional[int]
    visionWardsBoughtInGame: Optional[int]
    wardsKilled: Optional[int]
    wardsPlaced: Optional[int]
    win: Optional[bool]


class TeamDto(BaseModel):
    bans: List[BanDto]
    objectives: ObjectivesDto
    teamId: int
    win: bool


class InfoDto(BaseModel):
    endOfGameResult: Optional[str]
    gameCreation: int
    gameDuration: int
    gameEndTimestamp: Optional[int]
    gameId: int
    gameMode: str
    gameName: Optional[str]
    gameStartTimestamp: int
    gameType: str
    gameVersion: str
    mapId: int
    participants: List[ParticipantDto]
    platformId: str
    queueId: int
    teams: List[TeamDto]
    tournamentCode: Optional[str]


class MissionsDto(BaseModel):
    playerScore0: int
    playerScore1: int
    playerScore2: int
    playerScore3: int
    playerScore4: int
    playerScore5: int
    playerScore6: int
    playerScore7: int
    playerScore8: int
    playerScore9: int
    playerScore10: int
    playerScore11: int


class ChallengesDto(BaseModel):
    _12AssistStreakCount: Optional[int] = None
    baronBuffGoldAdvantageOverThreshold: Optional[int] = None
    controlWardTimeCoverageInRiverOrEnemyHalf: Optional[float] = None
    earliestBaron: Optional[int] = None
    earliestDragonTakedown: Optional[int] = None
    earliestElderDragon: Optional[int] = None
    earlyLaningPhaseGoldExpAdvantage: Optional[int] = None
    fasterSupportQuestCompletion: Optional[int] = None
    fastestLegendary: Optional[int] = None
    hadAfkTeammate: Optional[int] = None
    highestChampionDamage: Optional[int] = None
    highestCrowdControlScore: Optional[int] = None
    highestWardKills: Optional[int] = None
    junglerKillsEarlyJungle: Optional[int] = None
    killsOnLanersEarlyJungleAsJungler: Optional[int] = None
    laningPhaseGoldExpAdvantage: Optional[int] = None
    legendaryCount: Optional[int] = None
    maxCsAdvantageOnLaneOpponent: Optional[float] = None
    maxLevelLeadLaneOpponent: Optional[int] = None
    mostWardsDestroyedOneSweeper: Optional[int] = None
    mythicItemUsed: Optional[int] = None
    playedChampSelectPosition: Optional[int] = None
    soloTurretsLategame: Optional[int] = None
    takedownsFirst25Minutes: Optional[int] = None
    teleportTakedowns: Optional[int] = None
    thirdInhibitorDestroyedTime: Optional[int] = None
    threeWardsOneSweeperCount: Optional[int] = None
    visionScoreAdvantageLaneOpponent: Optional[float] = None
    InfernalScalePickup: Optional[int] = None
    fistBumpParticipation: Optional[int] = None
    voidMonsterKill: Optional[int] = None
    abilityUses: Optional[int] = None
    acesBefore15Minutes: Optional[int] = None
    alliedJungleMonsterKills: Optional[float] = None
    baronTakedowns: Optional[int] = None
    blastConeOppositeOpponentCount: Optional[int] = None
    bountyGold: Optional[int] = None
    buffsStolen: Optional[int] = None
    completeSupportQuestInTime: Optional[int] = None
    controlWardsPlaced: Optional[int] = None
    damagePerMinute: Optional[float] = None
    damageTakenOnTeamPercentage: Optional[float] = None
    dancedWithRiftHerald: Optional[int] = None
    deathsByEnemyChamps: Optional[int] = None
    dodgeSkillShotsSmallWindow: Optional[int] = None
    doubleAces: Optional[int] = None
    dragonTakedowns: Optional[int] = None
    legendaryItemUsed: Optional[List[int]] = None
    effectiveHealAndShielding: Optional[float] = None
    elderDragonKillsWithOpposingSoul: Optional[int] = None
    elderDragonMultikills: Optional[int] = None
    enemyChampionImmobilizations: Optional[int] = None
    enemyJungleMonsterKills: Optional[float] = None
    epicMonsterKillsNearEnemyJungler: Optional[int] = None
    epicMonsterKillsWithin30SecondsOfSpawn: Optional[int] = None
    epicMonsterSteals: Optional[int] = None
    epicMonsterStolenWithoutSmite: Optional[int] = None
    firstTurretKilled: Optional[int] = None
    firstTurretKilledTime: Optional[float] = None
    flawlessAces: Optional[int] = None
    fullTeamTakedown: Optional[int] = None
    gameLength: Optional[float] = None
    getTakedownsInAllLanesEarlyJungleAsLaner: Optional[int] = None
    goldPerMinute: Optional[float] = None
    hadOpenNexus: Optional[int] = None
    immobilizeAndKillWithAlly: Optional[int] = None
    initialBuffCount: Optional[int] = None
    initialCrabCount: Optional[int] = None
    jungleCsBefore10Minutes: Optional[float] = None
    junglerTakedownsNearDamagedEpicMonster: Optional[int] = None
    kda: Optional[float] = None
    killAfterHiddenWithAlly: Optional[int] = None
    killedChampTookFullTeamDamageSurvived: Optional[int] = None
    killingSprees: Optional[int] = None
    killParticipation: Optional[float] = None
    killsNearEnemyTurret: Optional[int] = None
    killsOnOtherLanesEarlyJungleAsLaner: Optional[int] = None
    killsOnRecentlyHealedByAramPack: Optional[int] = None
    killsUnderOwnTurret: Optional[int] = None
    killsWithHelpFromEpicMonster: Optional[int] = None
    knockEnemyIntoTeamAndKill: Optional[int] = None
    kTurretsDestroyedBeforePlatesFall: Optional[int] = None
    landSkillShotsEarlyGame: Optional[int] = None
    laneMinionsFirst10Minutes: Optional[int] = None
    lostAnInhibitor: Optional[int] = None
    maxKillDeficit: Optional[int] = None
    mejaisFullStackInTime: Optional[int] = None
    moreEnemyJungleThanOpponent: Optional[float] = None
    multiKillOneSpell: Optional[int] = None
    multikills: Optional[int] = None
    multikillsAfterAggressiveFlash: Optional[int] = None
    multiTurretRiftHeraldCount: Optional[int] = None
    outerTurretExecutesBefore10Minutes: Optional[int] = None
    outnumberedKills: Optional[int] = None
    outnumberedNexusKill: Optional[int] = None
    perfectDragonSoulsTaken: Optional[int] = None
    perfectGame: Optional[int] = None
    pickKillWithAlly: Optional[int] = None
    poroExplosions: Optional[int] = None
    quickCleanse: Optional[int] = None
    quickFirstTurret: Optional[int] = None
    quickSoloKills: Optional[int] = None
    riftHeraldTakedowns: Optional[int] = None
    saveAllyFromDeath: Optional[int] = None
    scuttleCrabKills: Optional[int] = None
    shortestTimeToAceFromFirstTakedown: Optional[float] = None
    skillshotsDodged: Optional[int] = None
    skillshotsHit: Optional[int] = None
    snowballsHit: Optional[int] = None
    soloBaronKills: Optional[int] = None
    soloKills: Optional[int] = None
    stealthWardsPlaced: Optional[int] = None
    survivedSingleDigitHpCount: Optional[int] = None
    survivedThreeImmobilizesInFight: Optional[int] = None
    takedownOnFirstTurret: Optional[int] = None
    takedowns: Optional[int] = None
    takedownsAfterGainingLevelAdvantage: Optional[int] = None
    takedownsBeforeJungleMinionSpawn: Optional[int] = None
    takedownsFirstXMinutes: Optional[int] = None
    takedownsInAlcove: Optional[int] = None
    takedownsInEnemyFountain: Optional[int] = None
    teamBaronKills: Optional[int] = None
    teamDamagePercentage: Optional[float] = None
    teamElderDragonKills: Optional[int] = None
    teamRiftHeraldKills: Optional[int] = None
    tookLargeDamageSurvived: Optional[int] = None
    turretPlatesTaken: Optional[int] = None
    turretsTakenWithRiftHerald: Optional[int] = None
    turretTakedowns: Optional[int] = None
    twentyMinionsIn3SecondsCount: Optional[int] = None
    twoWardsOneSweeperCount: Optional[int] = None
    unseenRecalls: Optional[int] = None
    visionScorePerMinute: Optional[float] = None
    wardsGuarded: Optional[int]


class MatchDto(BaseModel):
    metadata: MetadataDto
    info: InfoDto


class MetadataTimeLineDto(BaseModel):
    dataVersion: str
    matchId: str
    participants: List[str]


class ParticipantTimeLineDto(BaseModel):
    participantId: int
    puuid: str


class EventsTimeLineDto(BaseModel):
    timestamp: int
    realTimestamp: int
    type: str


class PositionDto(BaseModel):
    x: int
    y: int


class ChampionStatsDto(BaseModel):
    abilityHaste: int
    abilityPower: int
    armor: int
    armorPen: int
    armorPenPercent: int
    attackDamage: int
    attackSpeed: int
    bonusArmorPenPercent: int
    bonusMagicPenPercent: int
    ccReduction: int
    cooldownReduction: int
    health: int
    healthMax: int
    healthRegen: int
    lifesteal: int
    magicPen: int
    magicPenPercent: int
    magicResist: int
    movementSpeed: int
    omnivamp: int
    physicalVamp: int
    power: int
    powerMax: int
    powerRegen: int
    spellVamp: int


class DamageStatsDto(BaseModel):
    magicDamageDone: int
    magicDamageDoneToChampions: int
    magicDamageTaken: int
    physicalDamageDone: int
    physicalDamageDoneToChampions: int
    physicalDamageTaken: int
    totalDamageDone: int
    totalDamageDoneToChampions: int
    totalDamageTaken: int
    trueDamageDone: int
    trueDamageDoneToChampions: int
    trueDamageTaken: int


class ParticipantFrameDto(BaseModel):
    championStats: ChampionStatsDto
    currentGold: int
    damageStats: DamageStatsDto
    goldPerSecond: int
    jungleMinionsKilled: int
    level: int
    minionsKilled: int
    participantId: int
    position: PositionDto
    timeEnemySpentControlled: int
    totalGold: int
    xp: int


class ParticipantFramesDto(BaseModel):
    participantFrames: Dict[int, ParticipantFrameDto]


class FramesTimeLineDto(BaseModel):
    events: List[EventsTimeLineDto]
    participantFrames: ParticipantFramesDto
    timestamp: int


class InfoTimeLineDto(BaseModel):
    endOfGameResult: str
    frameInterval: int
    gameId: int
    participants: List[ParticipantTimeLineDto]
    frames: List[FramesTimeLineDto]


class TimelineDto(BaseModel):
    metadata: MetadataTimeLineDto
    info: InfoTimeLineDto


class MatchModel(str, Enum):
    """EUROPE, AMERICAS, ASIA, SEA"""

    EUROPE = "EUROPE"
    AMERICAS = "AMERICAS"
    ASIA = "ASIA"
    SEA = "SEA"


class MatchType(str, Enum):
    _all: str = "all"
    normal: str = "normal"
    ranked: str = "ranked"
    tournament: str = "tournament"
