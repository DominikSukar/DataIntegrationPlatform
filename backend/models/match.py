from enum import Enum


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
