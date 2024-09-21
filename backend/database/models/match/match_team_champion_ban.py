from sqlalchemy import ForeignKey, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column

from database.database import Base


class MatchTeamChampionBan(Base):
    """
    Table stores data about champion bans a team has made
    """
    __tablename__ = "match_team_champion_bans"

    id: Mapped[int] = mapped_column(primary_key=True)
    match_team_id: Mapped[int] = mapped_column(ForeignKey('match_teams.id'), nullable=False)
    champion_id: Mapped[int] = mapped_column(ForeignKey('champions.id'), nullable=False)
    ban_turn: Mapped[int] = mapped_column(SmallInteger, nullable=False)

    def __repr__(self):
        return f"<MatchTeamChampionBan(match_team_id='{self.match_team_id}', champion_id='{self.champion_id}', ban_turn='{self.ban_turn}')>"
