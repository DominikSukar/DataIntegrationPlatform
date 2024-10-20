from pydantic import BaseModel
from enum import Enum


class SummonerDTO(BaseModel):
    accountId: str
    profileIconId: int
    revisionDate: float
    id: str
    puuid: str
    summonerLevel: float


class SummonerAndSpectorServerModel(str, Enum):
    """EUW, EUNE, KR etc"""

    BR = "BR"
    EUNE = "EUNE"
    EUW = "EUW"
    JP = "JP"
    KR = "KR"
    LAN = "LAN"
    LAS = "LAS"
    ME = "ME"
    NA = "NA"
    OCE = "OCE"
    PH = "PH"
    RU = "RU"
    SG = "SG"
    TH = "TH"
    TR = "TR"
    TW = "TW"
    VN = "VN"
