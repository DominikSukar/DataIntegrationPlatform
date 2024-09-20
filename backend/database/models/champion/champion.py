from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from database.database import Base


class Champion(Base):
    """
    Table stores data about every champion
    """
    __tablename__ = "champions"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(20), nullable=False)

    def __repr__(self):
        return f"<Champion(name='{self.name}')>"
