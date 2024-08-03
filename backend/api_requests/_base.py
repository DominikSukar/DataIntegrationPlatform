from utils.env import *
from utils.domain_routers import get_mapped_server

class RiotAPIBase:
    KEY = f"?api_key={API_KEY}"

    def __init__(self, server: str, model):
        print(f">>>{server, model}")
        if not isinstance(server, model):
           print("1")
           self.server = get_mapped_server(server)
        else:
            print("2")
            self.server = server
        print(f">>>{self.server}")

    def get_domain(self, server: str):
        return globals().get(server)