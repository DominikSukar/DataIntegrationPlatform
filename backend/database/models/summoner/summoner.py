from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.database import Base


class Summoner(Base):
    __tablename__ = "summoners"

    id: Mapped[int] = mapped_column(primary_key=True)
    nickname: Mapped[str] = mapped_column(String(20), nullable=False)
    tag: Mapped[str] = mapped_column(String(5), nullable=False)
    server_id: Mapped[int] = mapped_column(Integer, ForeignKey("servers.id"))

    server: Mapped["Server"] = relationship(back_populates="summoner")


    def __repr__(self):
        return f"<Server(name='{self.name}', symbol='{self.symbol}', active='{self.active}')>"