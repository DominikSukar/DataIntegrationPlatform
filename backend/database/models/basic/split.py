from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from database.database import Base


class Split(Base):
    """
    Table stores data about all splits that database had archived matches from.
    """

    __tablename__ = "splits"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    season_id: Mapped[int] = mapped_column(ForeignKey("seasons.id"), nullable=False)

    def __repr__(self):
        return f"<Split(id='{self.id}', riot_match_id='{self.riot_match_id}')>"
