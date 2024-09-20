from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from database.database import Base


class MatchParticipantPerk(Base):
    """
    Table stores data about a perk that a specific match participant had
    """
    __tablename__ = "match_participant_perks"

    id: Mapped[int] = mapped_column(primary_key=True)
    match_participant_id: Mapped[int] = mapped_column(ForeignKey('match_participants.id'), nullable=False)
    perk_id: Mapped[int] = mapped_column(ForeignKey('perks.id'), nullable=False)

    def __repr__(self):
        return f"<MatchParticipantPerk(name='{self.name}')>"
