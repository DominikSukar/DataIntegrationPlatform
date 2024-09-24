from sqlalchemy import ForeignKey, Integer, SmallInteger, Boolean, String
from sqlalchemy.orm import Mapped, mapped_column

from database.database import Base


class MatchParticipant(Base):
    """
    Table stores data about ta specific team that participated in a game
    """

    __tablename__ = "match_participants"

    id: Mapped[int] = mapped_column(primary_key=True)
    summoner_id: Mapped[int] = mapped_column(ForeignKey("summoners.id"), nullable=False)
    match_id: Mapped[int] = mapped_column(ForeignKey("matches.id"), nullable=False)
    # 100 for blue, 200 for red
    team_id: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    match_team_id: Mapped[int] = mapped_column(
        ForeignKey("match_teams.id"), nullable=False
    )
    win: Mapped[bool] = mapped_column(Boolean, nullable=False)
    # Both individualPosition and teamPosition are computed by the game server and are different
    # versions of the most likely position played by a player.
    # The individualPosition is the best guess for which position the player actually played in isolation of anything else.
    # The teamPosition is the best guess for which position the player actually played if we add the constraint
    # that each team must have one top player, one jungle, one middle, etc.
    # Generally the recommendation is to use the teamPosition field over the individualPosition field.
    individual_position: Mapped[str] = mapped_column(String(20), nullable=False)
    team_position: Mapped[str] = mapped_column(String(20), nullable=False)
    objective_stolen: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    objective_stolen_assists: Mapped[int] = mapped_column(SmallInteger, nullable=False)

    champion_id: Mapped[int] = mapped_column(ForeignKey("champions.id"), nullable=False)
    champion_level: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    kills: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    deaths: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    assists: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    kda: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    kill_participation: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    total_minions_killed: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    vision_score: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    # This field is currently only utilized for Kayn's transformations. (Legal values: 0 - None, 1 - Slayer, 2 - Assassin)
    champion_transform: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    gold_earned: Mapped[int] = mapped_column(Integer, nullable=False)

    turret_kills: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    turret_takedown: Mapped[int] = mapped_column(SmallInteger, nullable=False)

    damage_to_champions: Mapped[int] = mapped_column(Integer, nullable=False)
    damage_to_objectives: Mapped[int] = mapped_column(Integer, nullable=False)
    damage_to_turrets: Mapped[int] = mapped_column(Integer, nullable=False)
    damage_self_mitigated: Mapped[int] = mapped_column(Integer, nullable=False)
    damage_taken: Mapped[int] = mapped_column(Integer, nullable=False)

    damage_shielded_to_champions: Mapped[int] = mapped_column(Integer, nullable=False)
    total_heals_on_teammates: Mapped[int] = mapped_column(Integer, nullable=False)

    item_0: Mapped[int] = mapped_column(ForeignKey("items.id"), nullable=False)
    item_1: Mapped[int] = mapped_column(ForeignKey("items.id"), nullable=False)
    item_2: Mapped[int] = mapped_column(ForeignKey("items.id"), nullable=False)
    item_3: Mapped[int] = mapped_column(ForeignKey("items.id"), nullable=False)
    item_4: Mapped[int] = mapped_column(ForeignKey("items.id"), nullable=False)
    item_5: Mapped[int] = mapped_column(ForeignKey("items.id"), nullable=False)
    item_6: Mapped[int] = mapped_column(ForeignKey("items.id"), nullable=False)

    def __repr__(self):
        return (
            f"<MatchParticipant(match_id='{self.match_id}', team_id='{self.team_id}')>"
        )
