from sqlalchemy import ForeignKey, Integer, SmallInteger, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from database.database import Base


class MatchParticipant(Base):
    """
    Table stores data about ta specific team that participated in a game
    """
    __tablename__ = "match_participants"

    id: Mapped[int] = mapped_column(primary_key=True)
    summoner_id: Mapped[str] = mapped_column(ForeignKey('summoners.id'), nullable=False)
    match_id: Mapped[int] = mapped_column(ForeignKey('matches.id'), nullable=False)
    champion_id: Mapped[int] = mapped_column(ForeignKey('champions.id'), nullable=False)
    # 100 for blue, 200 for red
    team_id: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    match_team_id: Mapped[int] = mapped_column(ForeignKey('match_teams.id'), nullable=False)
    kills: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    deaths: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    assists: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    kda: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    kill_participation: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    win: Mapped[bool] = mapped_column(Boolean, nullable=False)

    def __repr__(self):
        return f"<MatchParticipant(match_id='{self.match_id}', team_id='{self.team_id}')>"
