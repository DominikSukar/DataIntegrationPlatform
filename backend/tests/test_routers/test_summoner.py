import pytest

from fastapi.testclient import TestClient
from fastapi import HTTPException
from fastapi.exceptions import RequestValidationError

from routers.summoner import router

from schemas.summoner import SummonerDTO

client = TestClient(router)

class TestGetSummonerInfo:
    def test_by_providing_user_id(self):
        "Test endpoint by requesting data by providing combination of summoner_name and tag_line"
        REQUEST_PARAMS = {"summoner_name": "PrinceOfEssling", "tag_line": "EUW"}
        EXPECTED_STABLE_FIELDS  = {
            "id": "lWUIM6ChhgyyeccN5Z-CKFhX-WETnc19xTdetXkDO-W-sXI",
            "accountId": "y4m_h-DtfgBfRr5msXkwQHwFvEwyHR-kCJM-VCArJ2Q2fpI",
            "puuid": "Bh1lQALIiYypSsY1PGNULQhGCM6hy3ejaLmHiUZXbR84yPOuD7jMa9PhVlwI42mcdpteq-RYWNw-RA",
        }
        response = client.get("/", params=REQUEST_PARAMS)
        assert response.status_code == 200

        response_data = response.json()

        for key, value in EXPECTED_STABLE_FIELDS.items():
            assert response_data[key] == value

        SummonerDTO(**response_data)

    def test_by_providing_not_existing_user_id(self):
        "Test endpoint by requesting data by providing combination of summoner_name and tag_line"
        params = {"summoner_name": "sdasdsad", "tag_line": "sadsad"}

        with pytest.raises(HTTPException) as err:
            client.get("/", params=params)
        assert err.value.status_code == 404

    def test_by_providing_puuid(self):
        """Test endpoint by requesting data by providing user's puuid
        Testing 1:1 values only on stable keys, the rest is just checking if a key is even in response (SummonerDTO schema)"""
        REQUEST_PARAMS = {
            "puuid": "Bh1lQALIiYypSsY1PGNULQhGCM6hy3ejaLmHiUZXbR84yPOuD7jMa9PhVlwI42mcdpteq-RYWNw-RA"
        }
        EXPECTED_STABLE_FIELDS  = {
            "id": "lWUIM6ChhgyyeccN5Z-CKFhX-WETnc19xTdetXkDO-W-sXI",
            "accountId": "y4m_h-DtfgBfRr5msXkwQHwFvEwyHR-kCJM-VCArJ2Q2fpI",
            "puuid": "Bh1lQALIiYypSsY1PGNULQhGCM6hy3ejaLmHiUZXbR84yPOuD7jMa9PhVlwI42mcdpteq-RYWNw-RA",
        }
        response = client.get("/", params=REQUEST_PARAMS)
        assert response.status_code == 200

        response_data = response.json()

        for key, value in EXPECTED_STABLE_FIELDS.items():
            assert response_data[key] == value

        SummonerDTO(**response_data)


    def test_by_providing_not_existing_puuid(self):
        "Test endpoint by requesting data by puuid that is not decryptable or simply doesnt exist"
        params = {"puuid": "fdfsdfdsfsdfdsfs"}

        with pytest.raises(HTTPException) as err:
            client.get("/", params=params)
        assert err.value.status_code == 400
