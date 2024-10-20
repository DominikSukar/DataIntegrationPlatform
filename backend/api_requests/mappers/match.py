from datetime import datetime
from typing import List

from schemas import (
    MatchDto,
    ParticipantDto,
    TeamDto,
    InfoDto,
    BanDto,
    PerksDto,
)
from serializers.match.match import MatchResponse


def matches_mapper(match: MatchDto, server_id: int, split_id: int) -> MatchResponse:
    return {
        "riot_match_id": match["metadata"]["matchId"],
        "server_id": server_id,
        "game_result": match["info"]["endOfGameResult"],
        "creation_date": datetime.fromtimestamp(match["info"]["gameCreation"] / 1000),
        "end_date": datetime.fromtimestamp(match["info"]["gameEndTimestamp"] / 1000),
        "game_duration": match["info"]["gameDuration"],
        "split_id": split_id,
    }


def match_participants_mapper(
    participant: ParticipantDto,
    summoner_id: int,
    match_id: int,
    match_team_id: int,
    champion_id: int,
    items: List[int],
):
    return {
        "summoner_id": summoner_id,
        "match_id": match_id,
        "team_id": participant["teamId"],
        "match_team_id": match_team_id,
        "win": participant["win"],
        "individual_position": participant["individualPosition"],
        "team_position": participant["teamPosition"],
        "objective_stolen": participant["objectivesStolen"],
        "objective_stolen_assists": participant["objectivesStolenAssists"],
        "champion_id": champion_id,
        "champion_level": participant["champLevel"],
        "kills": participant["kills"],
        "deaths": participant["deaths"],
        "assists": participant["assists"],
        "kda": (
            int(
                (participant["kills"] + participant["assists"])
                / participant["deaths"]
                * 100
            )
            if participant["deaths"] != 0
            else (
                0 if participant["kills"] == 0 and participant["assists"] == 0 else 2137
            )
        ),
        "kill_participation": (
            int(participant["challenges"]["killParticipation"] * 100)
            if participant["challenges"].get("killParticipation") is not None
            else 0
        ),
        "total_minions_killed": participant["totalMinionsKilled"],
        "vision_score": participant["visionScore"],
        "champion_transform": participant["championTransform"],
        "gold_earned": participant["goldEarned"],
        "turret_kills": participant["turretKills"],
        "turret_takedown": participant["turretTakedowns"],
        "damage_to_champions": participant["totalDamageDealtToChampions"],
        "damage_to_objectives": participant["damageDealtToObjectives"],
        "damage_to_turrets": participant["damageDealtToTurrets"],
        "damage_self_mitigated": participant["damageSelfMitigated"],
        "damage_taken": participant["totalDamageTaken"],
        "damage_shielded_to_champions": participant["totalDamageShieldedOnTeammates"],
        "total_heals_on_teammates": participant["totalHealsOnTeammates"],
        "item_0": items[0],
        "item_1": items[1],
        "item_2": items[2],
        "item_3": items[3],
        "item_4": items[4],
        "item_5": items[5],
        "item_6": items[6],
    }


def match_teams_mapper(team: TeamDto, match_info: InfoDto, match_id: int):
    objectives = team["objectives"]
    return {
        "match_id": match_id,
        "team_id": team["teamId"],
        "damage_dealt": sum(
            [
                participant["totalDamageDealtToChampions"]
                for participant in match_info["participants"]
            ]
        ),
        "damage_taken": sum(
            [
                participant["totalDamageTaken"]
                for participant in match_info["participants"]
            ]
        ),
        "total_gold": sum(
            [participant["goldEarned"] for participant in match_info["participants"]]
        ),
        "towers_taken": objectives["tower"]["kills"],
        "dragons_taken": objectives["dragon"]["kills"],
        "barons_taken": objectives["baron"]["kills"],
        "krugs_taken": objectives["horde"]["kills"],
        "heralds_taken": objectives["riftHerald"]["kills"],
    }


def team_champion_bans_mapper(ban: BanDto, match_team_id: int, champion_id: int):
    return {
        "match_team_id": match_team_id,
        "champion_id": champion_id,
        "ban_turn": ban["pickTurn"],
    }


def match_participant_perks_mapper(perks: PerksDto, match_participant_id: int):
    returned_list = []

    for perk in perks["styles"]:
        if perk["description"] == "primaryStyle":
            is_primary = True
        elif perk["description"] == "subStyle":
            is_primary = False

        for index, selection in enumerate(perk["selections"]):
            returned_list.append(
                {
                    "is_primary": is_primary,
                    "is_style": False,
                    "slot": index,
                    "match_participant_id": match_participant_id,
                    "perk_id": selection["perk"],
                }
            )

        returned_list.append(
            {
                "is_primary": is_primary,
                "is_style": True,
                "slot": index,
                "match_participant_id": match_participant_id,
                "perk_id": perk["style"],
            }
        )

    return returned_list


def match_participant_summoner_spells_mapper(
    slot: int, match_participant_id: int, summoner_spell_id: int
):
    return {
        "slot": slot,
        "match_participant_id": match_participant_id,
        "summoner_spell_id": summoner_spell_id,
    }
