from datetime import datetime

from sqlalchemy import ForeignKey, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from database.database import Base


class Match(Base):
    """
    Table stores data about every match archived in the database
    """

    __tablename__ = "matches"

    id: Mapped[int] = mapped_column(primary_key=True)
    riot_match_id: Mapped[str] = mapped_column(String(50), nullable=False)
    server_id: Mapped[int] = mapped_column(ForeignKey("servers.id"), nullable=False)
    game_result: Mapped[str] = mapped_column(String, nullable=False)
    date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    season_id: Mapped[int] = mapped_column(ForeignKey("seasons.id"), nullable=False)

    def __repr__(self):
        return f"<Match(id='{self.id}', riot_match_id='{self.riot_match_id}'), date='{self.date}'>"
