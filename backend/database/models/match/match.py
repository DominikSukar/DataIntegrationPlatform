from datetime import datetime

from sqlalchemy import ForeignKey, SmallInteger, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from database.database import Base


class Match(Base):
    """
    Table stores data about every match archived in the database
    """

    __tablename__ = "matches"

    id: Mapped[int] = mapped_column(primary_key=True)
    riot_match_id: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    server_id: Mapped[int] = mapped_column(ForeignKey("servers.id"), nullable=False)
    game_result: Mapped[str] = mapped_column(String, nullable=False)
    creation_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False
    )
    end_date: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    game_duration: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    split_id: Mapped[int] = mapped_column(ForeignKey("splits.id"), nullable=False)

    def __repr__(self):
        return f"<Match(id='{self.id}', riot_match_id='{self.riot_match_id}'), game_duration='{self.game_duration}'>"
