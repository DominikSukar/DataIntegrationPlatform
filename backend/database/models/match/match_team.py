from sqlalchemy import ForeignKey, Integer, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column

from database.database import Base


class MatchTeam(Base):
    """
    Table stores data about ta specific team that participated in a game
    """

    __tablename__ = "match_teams"

    id: Mapped[int] = mapped_column(primary_key=True)
    match_id: Mapped[int] = mapped_column(ForeignKey("matches.id"), nullable=False)
    # 100 for blue, 200 for red
    team_id: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    damage_dealt: Mapped[int] = mapped_column(Integer, nullable=False)
    damage_taken: Mapped[int] = mapped_column(Integer, nullable=False)
    total_gold: Mapped[int] = mapped_column(Integer, nullable=False)
    towers_taken: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    dragons_taken: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    barons_taken: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    krugs_taken: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    herals_taken: Mapped[int] = mapped_column(SmallInteger, nullable=False)

    def __repr__(self):
        return f"<MatchTeam(match_id='{self.match_id}', team_id='{self.team_id}')>"
