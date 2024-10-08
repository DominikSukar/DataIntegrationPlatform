from datetime import datetime

from schemas.combined_schemas import LeagueAndSummonerEntryDTO


def convert_LeagueAndSummonerEntryDTO_to_Summoner(
    summoner_dto: LeagueAndSummonerEntryDTO, nickname: str, tag: str, server_id: int
) -> dict:
    return {
        "nickname": nickname,
        "tag": tag,
        "puuid": summoner_dto.puuid,
        "profile_icon_id": summoner_dto.profileIconId,
        "riot_id": summoner_dto.id,
        "account_id": summoner_dto.accountId,
        # riot's timestamp is in miliseconds, not seconds, so has to be devided
        "revision_date": datetime.fromtimestamp(summoner_dto.revisionDate / 1000),
        "last_update_date": datetime.now().replace(microsecond=0),
        "server_id": server_id,
        "tier": summoner_dto.tier,
        "rank": summoner_dto.rank,
        "lp": summoner_dto.leaguePoints,
        "matches_played": summoner_dto.wins + summoner_dto.losses,
        "matches_won": summoner_dto.wins,
        "winrate": summoner_dto.winrate,
    }
