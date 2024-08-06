from enum import Enum


class AccountModel(str, Enum):
    """EUROPE, AMERICAS, ASIA, ESPORTS"""

    EUROPE = "EUROPE"
    AMERICAS = "AMERICAS"
    ASIA = "ASIA"
    ESPORTS = "ESPORTS"
