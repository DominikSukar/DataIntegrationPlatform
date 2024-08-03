from enum import Enum
from pydantic import BaseModel

class AccountModel(str, Enum):
    EUROPE = "EUROPE"
    AMERICAS = "AMERICAS"
    ASIA = "ASIA"
    ESPORTS = "ESPORTS"