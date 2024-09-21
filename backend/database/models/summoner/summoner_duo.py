from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from database.database import Base


class SummonerDuo(Base):
    """
    Table stores data about how many times each player played with another player
    """
    __tablename__ = "summoner_duos"

    id: Mapped[int] = mapped_column(primary_key=True)
    summoner_id: Mapped[int] = mapped_column(Integer, ForeignKey("summoners.id"), nullable=False)
    duo_id: Mapped[int] = mapped_column(Integer, ForeignKey("summoners.id"), nullable=False)
    matches_played: Mapped[int] = mapped_column(Integer, nullable=False)

    def __repr__(self):
        return f"<SummonerDuo(summoner_id='{self.summoner_id}', duo_id='{self.duo_id}', matches_played='{self.matches_played}')>"
