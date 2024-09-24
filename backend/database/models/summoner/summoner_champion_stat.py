from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from database.database import Base


class SummonerChampionStat(Base):
    """
    Table stores data about summoner's statistics on a specific champion
    """

    __tablename__ = "summoner_champion_stats"

    id: Mapped[int] = mapped_column(primary_key=True)
    summoner_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("summoners.id"), nullable=False
    )
    champion_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("champions.id"), nullable=False
    )
    matches_played: Mapped[int] = mapped_column(Integer, nullable=False)
    matches_won: Mapped[int] = mapped_column(Integer, nullable=False)
    winrate: Mapped[int] = mapped_column(Integer, nullable=False)

    def __repr__(self):
        return f"<SummonerChampionStat(summoner_id='{self.summoner_id}', champion_id='{self.champion_id}, matches_played='{self.matches_played}')>"
