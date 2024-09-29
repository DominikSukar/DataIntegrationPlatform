from sqlalchemy import ForeignKey, Integer, SmallInteger, Float, String
from sqlalchemy.orm import Mapped, mapped_column

from database.database import Base


class Summoner(Base):
    """
    Table stores data about every summoner
    """

    __tablename__ = "summoners"

    id: Mapped[int] = mapped_column(primary_key=True)
    nickname: Mapped[str] = mapped_column(String(20), nullable=False)
    tag: Mapped[str] = mapped_column(String(5), nullable=False)
    server_id: Mapped[int] = mapped_column(Integer, ForeignKey("servers.id"))
    rank: Mapped[str] = mapped_column(String(20), nullable=False)
    lp = Mapped[int] = mapped_column(SmallInteger, nullable=False)
    matches_played = Mapped[int] = mapped_column(SmallInteger, nullable=False)
    matched_won = Mapped[int] = mapped_column(SmallInteger, nullable=False)
    winrate = Mapped[int] = mapped_column(Float, nullable=False)

    def __repr__(self):
        return f"<Summoner(nickname='{self.nickname}', tag='{self.tag}', server_id='{self.server_id}')>"
