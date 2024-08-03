

class RiotAPIBase:
    BASE_URL = "https://example.api.riotgames.com"
    API_KEY = "your_api_key_here"

    DOMAIN = DOMAIN_EUROPE + "/riot/account/v1"
    key = f"?api_key={API_KEY}"

    def _make_request(self, endpoint: str, params: dict = None):
        headers = {"X-Riot-Token": self.API_KEY}
        response = requests.get(f"{self.BASE_URL}/{endpoint}", headers=headers, params=params)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()