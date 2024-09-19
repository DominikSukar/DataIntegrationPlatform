from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.database import Base


class Server(Base):
    """
    Table stores data about every RIOT server.
    """
    __tablename__ = "servers"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    symbol: Mapped[str] = mapped_column(String(5), nullable=False)
    active: Mapped[bool] = mapped_column(Boolean, nullable=False)

    def __repr__(self):
        return f"<Server(name='{self.name}', symbol='{self.symbol}', active='{self.active}')>"
