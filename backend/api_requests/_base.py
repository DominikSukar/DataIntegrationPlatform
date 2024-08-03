from utils.env import *
from utils.domain_routers import get_mapped_server

class RiotAPIBase:
    KEY = f"?api_key={API_KEY}"

    def __init__(self, server: str, model):
        if not isinstance(server, model):
           self.server = get_mapped_server(server)
        else:
            self.server = server

    def get_domain(self, server: str):
        return globals().get(server)