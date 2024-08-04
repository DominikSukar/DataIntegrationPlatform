from enum import Enum


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
