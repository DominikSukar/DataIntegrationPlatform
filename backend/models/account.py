from enum import Enum
from pydantic import BaseModel

class AccountModel(str, Enum):
    """EUROPE, AMERICAS, ASIA, ESPORTS"""
    EUROPE = "EUROPE"
    AMERICAS = "AMERICAS"
    ASIA = "ASIA"
    ESPORTS = "ESPORTS"