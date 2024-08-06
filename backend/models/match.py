from enum import Enum


class MatchModel(str, Enum):
    """EUROPE, AMERICAS, ASIA, SEA"""

    EUROPE = "EUROPE"
    AMERICAS = "AMERICAS"
    ASIA = "ASIA"
    SEA = "SEA"
