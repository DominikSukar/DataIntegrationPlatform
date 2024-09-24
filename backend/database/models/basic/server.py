from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column

from database.database import Base


class Server(Base):
    """
    Table stores data about every RIOT server.
    """

    __tablename__ = "servers"

    id: Mapped[int] = mapped_column(primary_key=True)
    # Europe Nordic and East
    full_name: Mapped[str] = mapped_column(String(50), nullable=False)
    # EUNE
    symbol: Mapped[str] = mapped_column(String(5), nullable=False)
    # EUN1
    riot_symbol: Mapped[str] = mapped_column(String(5), nullable=False)
    # eun1.api.riotgames.com
    hostname: Mapped[str] = mapped_column(String(50), nullable=False)
    active: Mapped[bool] = mapped_column(Boolean, nullable=False)

    def __repr__(self):
        return f"<Server(name='{self.full_name}', symbol='{self.symbol}', active='{self.active}')>"
