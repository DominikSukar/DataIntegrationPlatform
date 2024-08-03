import pytest

from fastapi.testclient import TestClient
from fastapi import HTTPException
from fastapi.exceptions import RequestValidationError

from routers.account import router

client = TestClient(router)


class TestGetAccountPUUID:
    def test_existing_user(self):
        "Test for user that exists"
        params = {
            "summoner_name": "PrinceOfEssling",
            "tag_line": "EUW",
            "server": "EUROPE",
        }
        response = client.get("/get_puuid", params=params)
        assert response.status_code == 200

    def test_not_existing_user(self):
        "Test for user that should not exist"
        params = {"summoner_name": "sdssdsdsd", "tag_line": "NAE", "server": "EUROPE"}

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


class TestGetAccountInfo:
    def test_by_providing_user_id(self):
        "Test endpoint by requesting data by providing combination of summoner_name and tag_line"
        params = {
            "summoner_name": "PrinceOfEssling",
            "tag_line": "EUW",
            "server": "EUROPE",
        }
        response = client.get("/info", params=params)
        assert response.status_code == 200
        assert response.json() == {
            "gameName": "PrinceOfEssling",
            "tagLine": "EUW",
            "puuid": "Bh1lQALIiYypSsY1PGNULQhGCM6hy3ejaLmHiUZXbR84yPOuD7jMa9PhVlwI42mcdpteq-RYWNw-RA",
        }

    def test_by_providing_not_existing_user_id(self):
        "Test endpoint by requesting data by providing combination of summoner_name and tag_line"
        params = {"summoner_name": "sdasdsad", "tag_line": "sadsad", "server": "EUROPE"}

        with pytest.raises(HTTPException) as err:
            client.get("/info", params=params)
        assert err.value.status_code == 404

    def test_by_providing_puuid(self):
        "Test endpoint by requesting data by providing user's puuid"
        params = {
            "puuid": "Bh1lQALIiYypSsY1PGNULQhGCM6hy3ejaLmHiUZXbR84yPOuD7jMa9PhVlwI42mcdpteq-RYWNw-RA",
            "server": "EUROPE",
        }
        response = client.get("/info", params=params)
        assert response.status_code == 200
        assert response.json() == {
            "gameName": "PrinceOfEssling",
            "tagLine": "EUW",
            "puuid": "Bh1lQALIiYypSsY1PGNULQhGCM6hy3ejaLmHiUZXbR84yPOuD7jMa9PhVlwI42mcdpteq-RYWNw-RA",
        }

    def test_by_providing_not_existing_puuid(self):
        "Test endpoint by requesting data by puuid that is not decryptable or simply doesnt exist"
        params = {"puuid": "fdfsdfdsfsdfdsfs", "server": "EUROPE"}

        with pytest.raises(HTTPException) as err:
            client.get("/info", params=params)
        assert err.value.status_code == 400
