from schemas.combined_schemas import LeagueAndSummonerEntryDTO


def convert_LeagueAndSummonerEntryDTO_to_Summoner(
    summoner_dto: LeagueAndSummonerEntryDTO, tag: str, server_id: int
) -> dict:
    return {
        "nickname": summoner_dto.id,
        "tag": None,
        "puuid": summoner_dto.puuid,
        "profile_icon_id": summoner_dto.profileIconId,
        "riot_id": summoner_dto.accountId,
        "account_id": summoner_dto.accountId,
        "revision_date": summoner_dto.revisionDate,
        "server_id": server_id,
        "tier": summoner_dto.tier,
        "rank": summoner_dto.rank,
        "lp": summoner_dto.leaguePoints,
        "matches_played": summoner_dto.wins + summoner_dto.losses,
        "matched_won": summoner_dto.wins,
        "winrate": summoner_dto.winrate,
    }
