import logging

from ._base import RiotAPIBase
from utils.requests import send_request
from models import AccountModel
from schemas import AccountDto

logger = logging.getLogger(__name__)


class AccountController(RiotAPIBase):
    "Class manages the Riot's API 'ACCOUNT-V1' service. As of 07.20.2024 there are 4 endpoints."

    PATH = "/riot/account/v1"

    def __init__(self, server: AccountModel):
        super().__init__(server, AccountModel)
        domain = super().get_domain(self.server)
        key = super().KEY
        self.url_account_by_puuid = "{}{}/accounts/by-puuid/{}{}".format(
            domain, self.PATH, "{puuid}", key
        )
        self.url_account_by_riot_ID = "{}{}/accounts/by-riot-id/{}/{}{}".format(
            domain, self.PATH, "{game_name}", "{tag_line}", key
        )
        self.url_active_shard_for_a_player = (
            "{}/active-shard/by-game{}{}/by-puuid/{}{}".format(
                domain, self.PATH, "{game}", "{puuid}", key
            )
        )
        self.url_account_by_access_token = "{}{}/accounts/me{}".format(
            domain, self.PATH, key
        )

    def get_account_by_puuid(self, puuid: str) -> AccountDto:
        "Provide summoner's PUUID, get dict of nickname, tag_line and puuid"
        URL = self.url_account_by_puuid.format(puuid=puuid)

        summoner_info = send_request(URL)
        summoner_info = AccountDto.model_validate(summoner_info)

        logging.debug(f"get_account_by_puuid > summoner_info: {summoner_info}")

        return summoner_info

    def get_account_by_riot_id(self, summoner_name: str, tag_line: str) -> str:
        "Provide summoner's nickname and tag, get PUUID in return"
        URL = self.url_account_by_riot_ID.format(
            game_name=summoner_name, tag_line=tag_line
        )

        summoner_info = send_request(URL)
        puuid = summoner_info["puuid"]

        logger.debug(f"PUUID {puuid} found for user {summoner_name}#{tag_line}")

        return puuid

    def get_active_shard_for_a_player(self, game: str, puuid: str):
        """This endpoint could be used on any REGION to look for a player in the different regions
        Parameter 'game' is equal to 'var' od 'lor' (Valorant and Legends of Runeterra)
        """
        URL = self.url_active_shard_for_a_player.format(game=game, puuid=puuid)
        pass

    def get_account_by_access_token(self):
        """CANNOT EXECUTE. THIS API ENDPOINT IS NOT AVAILABLE IN YOUR POLICY"""
        URL = self.url_account_by_access_token
        pass
