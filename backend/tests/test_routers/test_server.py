import pytest

from tests.setup import mock_client

@pytest.fixture(scope="class")
def sample_server_data():
    "Sample fixture returns an examplary server data"
    return {
        "full_name": "Europe Nordic and East",
        "symbol": "EUNE",
        "riot_symbol": "EUN1",
        "hostname": "eun1.api.riotgames.com",
        "active": True,
    }


class TestServerAPI:
    @pytest.fixture(scope="class")
    def setup_response(self, mock_client, sample_server_data):
        "Method uses POST to create server data based on a sample and returns the server's response"
        response = mock_client.post("/server/", json=sample_server_data)
        assert response.status_code == 201

        return response.json()

    def test_post(self, sample_server_data, setup_response):

        assert setup_response["full_name"] == sample_server_data["full_name"]
        assert setup_response["symbol"] == sample_server_data["symbol"]
        assert setup_response["riot_symbol"] == sample_server_data["riot_symbol"]
        assert setup_response["hostname"] == sample_server_data["hostname"]
        assert setup_response["active"] == sample_server_data["active"]

    def test_list(self, mock_client):
        response = mock_client.get("/server/")
        assert response.status_code == 200

