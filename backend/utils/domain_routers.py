from schemas import SummonerAndSpectorServerModel, MatchModel


def get_mapped_server(server: SummonerAndSpectorServerModel) -> MatchModel:
    routing_map = {
        "NA": "AMERICAS",
        "BR": "AMERICAS",
        "LAN": "AMERICAS",
        "LAS": "AMERICAS",
        "KR": "ASIA",
        "JP": "ASIA",
        "EUNE": "EUROPE",
        "EUW": "EUROPE",
        "ME": "EUROPE",
        "TR": "EUROPE",
        "RU": "EUROPE",
        "OCE": "SEA",
        "PH": "SEA",
        "SG": "SEA",
        "TH": "SEA",
        "TW": "SEA",
        "VN": "SEA",
    }

    return routing_map.get(server)
