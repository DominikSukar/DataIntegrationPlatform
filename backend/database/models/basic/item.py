from sqlalchemy import String, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column

from database.database import Base


class Item(Base):
    """
    Table stores data about every item
    """
    __tablename__ = "items"

    id: Mapped[int] = mapped_column(primary_key=True)
    riot_id: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    name: Mapped[str] = mapped_column(String(20), nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    cost: Mapped[int] = mapped_column(SmallInteger, nullable=False)

    def __repr__(self):
        return f"<Item(name='{self.name}')>"
