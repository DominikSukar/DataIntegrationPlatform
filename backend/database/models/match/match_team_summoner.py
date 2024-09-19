from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from database.database import Base


class MatchTeamSummoner(Base):
    """
    Junction table for a team and a summoner that was a part of it
    """
    __tablename__ = "match_team_summoners"

    id: Mapped[int] = mapped_column(primary_key=True)
    summoner_id: Mapped[str] = mapped_column(Integer, ForeignKey("summoners.id"), nullable=False)
    match_team_id: Mapped[str] = mapped_column(Integer, ForeignKey("match_team.id"), nullable=False)

    def __repr__(self):
        return f"<MatchTeamSummoner(summoner_id='{self.summoner_id}', match_team_id='{self.match_team_id}')>"
