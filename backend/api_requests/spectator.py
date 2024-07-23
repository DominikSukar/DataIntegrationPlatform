import logging

from schemas import CurrentGameInfo

from utils.env import API_KEY, DOMAIN_EUW1
from utils.requests import send_request

logger = logging.getLogger(__name__)


class SpectatorController:
    """Class manages the Riot's API 'SPECTATOR-V5' service. As of 07.20.2024 there are 2 endpoints.
    Every method is called by their RIOT respesctive counterparts"""

    "Please note that spectator-v5 service uses euw1 domain"
    DOMAIN = DOMAIN_EUW1 + "/lol/spectator/v5"
    key = f"?api_key={API_KEY}"

    url_current_game_information = "{}/active-games/by-summoner/{}{}".format(
        DOMAIN, "{puuid}", key
    )
    url_list_of_featured_games = "{}/featured-games{}".format(DOMAIN, key)


    def get_current_game_information__for_the_given_puuid(
        self, puuid: str
    ) -> CurrentGameInfo:
        "Endpoint gives data about a game that is going on currently"

        URL = self.url_current_game_information.format(puuid=puuid)

        game_info = send_request(URL)
        game_info = CurrentGameInfo.model_validate(game_info)

        logging.debug(
            f"get_current_game_information__for_the_given_puuid > game_info: {game_info}"
        )

        return game_info

    def get_list_of_featured_games(self):
        "Endpoint not planned to be used"

        URL = self.url_list_of_featured_games

        featured_games = send_request(URL)

        logging.debug(f"get_list_of_featured_games > featured_games: {featured_games}")

        return featured_games
