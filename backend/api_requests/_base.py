from utils.env import *

class RiotAPIBase:
    KEY = f"?api_key={API_KEY}"

    def get_domain(self, server: str):
        return globals().get(server)