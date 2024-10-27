from sqlalchemy import ForeignKey, Boolean, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.database import Base


class MatchParticipantPerk(Base):
    """
    Table stores data about a perk that a specific match participant had
    """

    __tablename__ = "match_participant_perks"

    id: Mapped[int] = mapped_column(primary_key=True)
    is_primary: Mapped[bool] = mapped_column(Boolean, nullable=False)
    is_style: Mapped[bool] = mapped_column(Boolean, nullable=False)
    slot: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    match_participant_id: Mapped[int] = mapped_column(
        ForeignKey("match_participants.id"), nullable=False
    )
    perk_id: Mapped[int] = mapped_column(ForeignKey("perks.id"), nullable=False)

    perk_data = relationship("Perk", back_populates="match_participant_perks")
    match_participants = relationship("MatchParticipant", back_populates="perks")

    def __repr__(self):
        return f"<MatchParticipantPerk(name='{self.name}')>"
