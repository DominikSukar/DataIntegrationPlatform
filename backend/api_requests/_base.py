from utils.env import *
from utils.domain_routers import get_mapped_server


class RiotAPIBase:
    KEY = f"?api_key={API_KEY}"

    def get_domain(self, server: str):
        return globals().get(server)
