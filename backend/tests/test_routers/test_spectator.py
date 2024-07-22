import pytest

from fastapi.testclient import TestClient
from fastapi import HTTPException
from fastapi.exceptions import RequestValidationError

from routers.spectator import router

from api_requests.spectator import SpectatorController

client = TestClient(router)

@pytest.fixture
def random_user():
    """Fixture is supposed to return a user that is currently in a game. 
    It is necessary to properly test API endpoints"""
    controller = SpectatorController()
    featured_games = controller.get_list_of_featured_games()
    if featured_games["gameList"]:
        user = featured_games["gameList"][0]["participants"][0]["riotId"]
        user_id, user_tag = user.split("#", 1)

        return user_id, user_tag
    
    raise Exception("No user in a game found. RIOT API is most likely down.")

class TestGetCurrentMatch:
    def test_existing_user(self, random_user):
        "Test for user that exists"
        user_id, user_tag = random_user

        params = {"summoner_name": user_id, "tag_line": user_tag}
        
        response = client.get("/", params=params)
        assert response.status_code == 200

    def test_not_existing_user(self):
        "Test for user that should not exist"
        params = {"summoner_name": "sdasdsad", "tag_line": "sadsad"}

        with pytest.raises(HTTPException) as err:
            client.get("/", params=params)
        assert err.value.status_code == 404        