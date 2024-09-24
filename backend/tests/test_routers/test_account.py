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
        }
        response = client.get("/EUW/get_puuid", params=params)
        assert response.status_code == 200

    def test_not_existing_user(self):
        "Test for user that should not exist"
        params = {"summoner_name": "sdssd2174sdsd", "tag_line": "EUW"}

        with pytest.raises(HTTPException) as err:
            client.get("/EUW/get_puuid", params=params)
        assert err.value.status_code == 404

    def test_no_parameters(self):
        "Makes sure that API's params are set as required"
        params = {}

        with pytest.raises(RequestValidationError) as err:
            client.get("/EUW/get_puuid", params=params)
        errors = err.value.errors()

        for error in errors:
            assert error["type"] == "missing"
            assert error["msg"] == "Field required"
            assert error["input"] is None


class TestGetAccountInfo:
    def test_by_providing_summoner_name(self):
        "Test endpoint by requesting data by providing only summoner_name"
        params = {
            "summoner_name": "PrinceOfEssling",
        }
        response = client.get("EUW//info", params=params)
        assert response.status_code == 200
        assert response.json() == {
            "gameName": "PrinceOfEssling",
            "tagLine": "EUW",
            "puuid": "Bh1lQALIiYypSsY1PGNULQhGCM6hy3ejaLmHiUZXbR84yPOuD7jMa9PhVlwI42mcdpteq-RYWNw-RA",
        }

    def test_by_providing_summoner_name_with_tag_line(self):
        "Test endpoint by requesting data by providing only summoner_name, but with tag inside"
        params = {
            "summoner_name": "PrinceOfEssling_EUW",
        }
        response = client.get("/EUW/info", params=params)
        assert response.status_code == 200
        assert response.json() == {
            "gameName": "PrinceOfEssling",
            "tagLine": "EUW",
            "puuid": "Bh1lQALIiYypSsY1PGNULQhGCM6hy3ejaLmHiUZXbR84yPOuD7jMa9PhVlwI42mcdpteq-RYWNw-RA",
        }

    def test_by_providing_not_existing_summoner_name(self):
        "Test endpoint by requesting data by providing summoner_name that (should!) not exist"
        params = {"summoner_name": "63cburlhqa", "server": "EUW"}

        with pytest.raises(HTTPException) as err:
            client.get("/EUW/info", params=params)
        assert err.value.status_code == 404

    def test_by_providing_puuid(self):
        "Test endpoint by requesting data by providing user's puuid"
        params = {
            "puuid": "Bh1lQALIiYypSsY1PGNULQhGCM6hy3ejaLmHiUZXbR84yPOuD7jMa9PhVlwI42mcdpteq-RYWNw-RA",
            "server": "EUW",
        }
        response = client.get("/EUW/info", params=params)
        assert response.status_code == 200
        assert response.json() == {
            "gameName": "PrinceOfEssling",
            "tagLine": "EUW",
            "puuid": "Bh1lQALIiYypSsY1PGNULQhGCM6hy3ejaLmHiUZXbR84yPOuD7jMa9PhVlwI42mcdpteq-RYWNw-RA",
        }

    def test_by_providing_not_existing_puuid(self):
        "Test endpoint by requesting data by puuid that is not decryptable or simply doesnt exist"
        params = {"puuid": "fdfsdfdsfsdfdsfs", "server": "EUW"}

        with pytest.raises(HTTPException) as err:
            client.get("/EUW/info", params=params)
        assert err.value.status_code == 400
