import pytest

from fastapi.testclient import TestClient
from fastapi import HTTPException
from fastapi.exceptions import RequestValidationError

from routers.account import router

client = TestClient(router)

class TestGetSummonerPUUID:
    def test_existing_user(self):
        "Test for user that exists"
        params = {
            "summoner_name": "PrinceOfEssling",
            "tag_line": "EUW"
        }
        response = client.get("/get_puuid", params=params)
        assert response.status_code == 200

    def test_not_existing_user(self):
        "Test for user that should not exist"
        params = {
             "summoner_name": "sdasdsad",
             "tag_line": "sadsad"
         }

        with pytest.raises(HTTPException) as err:
            client.get("/get_puuid", params=params)
        assert err.value.status_code == 404

    def test_no_parameters(self):
        "Test for user that should not exist"
        params = {}

        with pytest.raises(RequestValidationError) as err:
            client.get("/get_puuid", params=params)
        errors = err.value.errors()
        
        for error in errors:
            assert error["type"] == "missing"
            assert error["msg"] == "Field required"
            assert error["input"] == None
            