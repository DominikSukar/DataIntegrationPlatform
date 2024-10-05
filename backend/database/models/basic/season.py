from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from database.database import Base


class Season(Base):
    """
    Table stores data about all seasons that database had archived matches from.
    """

    __tablename__ = "seasons"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)

    def __repr__(self):
        return f"<Season(id='{self.id}', name='{self.name}')>"
