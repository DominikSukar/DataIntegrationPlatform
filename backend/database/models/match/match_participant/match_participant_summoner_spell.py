from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from database.database import Base


class MatchParticipantSummonerSpell(Base):
    """
    Table stores data about a summoner spells that a specific match participant had
    """
    __tablename__ = "match_participant_summoner_spells"

    id: Mapped[int] = mapped_column(primary_key=True)
    match_participant_id: Mapped[int] = mapped_column(ForeignKey('match_participants.id'), nullable=False)
    summoner_spell_id: Mapped[int] = mapped_column(ForeignKey('summoner_spells.id'), nullable=False)

    def __repr__(self):
        return f"<MatchParticipantSummonerSpell(name='{self.name}')>"
