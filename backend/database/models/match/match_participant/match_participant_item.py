from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from database.database import Base


class MatchParticipantSummonerItem(Base):
    """
    Table stores data about an item that a specific match participant had
    """
    __tablename__ = "match_participant_summoner_items"

    id: Mapped[int] = mapped_column(primary_key=True)
    match_participant_id: Mapped[int] = mapped_column(ForeignKey('match_participants.id'), nullable=False)
    item_id: Mapped[int] = mapped_column(ForeignKey('items.id'), nullable=False)

    def __repr__(self):
        return f"<MatchParticipantSummonerItem(name='{self.name}')>"
