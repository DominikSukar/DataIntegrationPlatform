from sqlalchemy import ForeignKey, BigInteger, Integer, SmallInteger, Float, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.database import Base


class Summoner(Base):
    """
    Table stores data about every summoner
    """

    __tablename__ = "summoners"

    id: Mapped[int] = mapped_column(primary_key=True)
    nickname: Mapped[str] = mapped_column(String(20), nullable=False)
    tag: Mapped[str] = mapped_column(String(5), nullable=False)
    puuid: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    profile_icon_id: Mapped[int] = mapped_column(Integer, nullable=False)
    riot_id: Mapped[int] = mapped_column(Integer, nullable=False)
    account_id: Mapped[int] = mapped_column(Integer, nullable=False)
    revision_date: Mapped[int] = mapped_column(BigInteger, nullable=False)

    server_id: Mapped[int] = mapped_column(Integer, ForeignKey("servers.id"))
    tier: Mapped[str] = mapped_column(String(20), nullable=False)
    rank: Mapped[str] = mapped_column(String(5), nullable=False)
    lp: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    matches_played: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    matched_won: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    winrate: Mapped[int] = mapped_column(Float, nullable=False)

    server = relationship("Server", back_populates="summoners")

    def __repr__(self):
        return f"<Summoner(nickname='{self.nickname}', tag='{self.tag}', server_id='{self.server_id}')>"
