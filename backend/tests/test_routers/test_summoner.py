import pytest

from fastapi.testclient import TestClient
from fastapi import HTTPException

from routers.summoner import router

from schemas.summoner import SummonerDTO

client = TestClient(router)


class TestGetSummonerInfo:
    def test_by_providing_summoner_name(self, sample_summoner_data):
        "Test endpoint by requesting data by providing combination of summoner_name and tag_line"
        REQUEST_PARAMS = {"summoner_name": "PrinceOfEssling"}
        EXPECTED_STABLE_FIELDS = {
            "id": sample_summoner_data["id"],
            "accountId": sample_summoner_data["accountId"],
            "puuid": sample_summoner_data["puuid"],
        }
        response = client.get("EUW/", params=REQUEST_PARAMS)
        assert response.status_code == 200

        response_data = response.json()

        for key, value in EXPECTED_STABLE_FIELDS.items():
            assert response_data[key] == value

        SummonerDTO(**response_data)

    def test_by_providing_not_existing_user_id(self):
        "Test endpoint by requesting data by providing combination of summoner_name and tag_line"
        params = {"summoner_name": "63cburlhqa"}

        with pytest.raises(HTTPException) as err:
            client.get("EUW/", params=params)
        assert err.value.status_code == 404

    def test_by_providing_puuid(self, sample_summoner_data):
        """Test endpoint by requesting data by providing user's puuid
        Testing 1:1 values only on stable keys, the rest is just checking if a key is even in response (SummonerDTO schema)
        """
        REQUEST_PARAMS = {"puuid": sample_summoner_data["puuid"]}
        EXPECTED_STABLE_FIELDS = {
            "id": sample_summoner_data["id"],
            "accountId": sample_summoner_data["accountId"],
            "puuid": sample_summoner_data["puuid"],
        }
        response = client.get("EUW/", params=REQUEST_PARAMS)
        assert response.status_code == 200

        response_data = response.json()

        for key, value in EXPECTED_STABLE_FIELDS.items():
            assert response_data[key] == value

        SummonerDTO(**response_data)

    def test_by_providing_not_existing_puuid(self):
        "Test endpoint by requesting data by puuid that is not decryptable or simply doesnt exist"
        params = {"puuid": "fdfsdfdsfsdfdsfs", "server": "EUW"}

        with pytest.raises(HTTPException) as err:
            client.get("EUW/", params=params)
        assert err.value.status_code == 400
