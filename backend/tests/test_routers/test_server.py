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
    def created_server(self, mock_client, sample_server_data):
        """
        Method uses POST to create server data based on a sample and returns the server's response.
        It is used in future tests:
        test_post - to check if returned data equals the one used to create an object
        test_get, test_patch, test_delete - to use returned 'id' attribute.
        """
        response = mock_client.post("/server/", json=sample_server_data)
        assert response.status_code == 201

        return response.json()

    def test_post(self, sample_server_data, created_server):
        """
        Test only checks id data created by created_server fixture does equal 
        to data used to create an object.
        """

        assert created_server["full_name"] == sample_server_data["full_name"]
        assert created_server["symbol"] == sample_server_data["symbol"]
        assert created_server["riot_symbol"] == sample_server_data["riot_symbol"]
        assert created_server["hostname"] == sample_server_data["hostname"]
        assert created_server["active"] == sample_server_data["active"]

    def test_list(self, mock_client, sample_server_data):
        """
        List GET endpoint should return a list with only one object.
        Furthermore, we have to delete the 'id' key returned after creating object.
        """
        response = mock_client.get("/server/")
        assert response.status_code == 200

        first_object = response.json()[0]
        # We check for 6 keys since 'id' should be returned as well (so 5+1 keys)
        assert len(first_object) == 6

        assert "id" in first_object
        assert first_object["full_name"] == sample_server_data["full_name"]
        assert first_object["symbol"] == sample_server_data["symbol"]
        assert first_object["riot_symbol"] == sample_server_data["riot_symbol"]
        assert first_object["hostname"] == sample_server_data["hostname"]
        assert first_object["active"] == sample_server_data["active"]

    def test_get(self, mock_client, sample_server_data, created_server):
        """
        GET endpoint returns specific object from the database
        """
        response = mock_client.get(f"/server/{created_server["id"]}")
        assert response.status_code == 200

        returned_object = response.json()
        # We check for 6 keys since 'id' should be returned as well (so 5+1 keys)
        assert len(returned_object) == 6
        
        assert "id" in returned_object
        assert returned_object["full_name"] == sample_server_data["full_name"]
        assert returned_object["symbol"] == sample_server_data["symbol"]
        assert returned_object["riot_symbol"] == sample_server_data["riot_symbol"]
        assert returned_object["hostname"] == sample_server_data["hostname"]
        assert returned_object["active"] == sample_server_data["active"]

    def test_patch(self, mock_client, created_server, sample_server_data):
        """
        PATCH test will update the 'active' attribute from 'True' to 'False'
        """
        update_data = {"active": False}
        response = mock_client.patch(f"/server/{created_server['id']}", json=update_data)
        assert response.status_code == 200

        returned_object = response.json()
        # We check for 6 keys since 'id' should be returned as well (so 5+1 keys)
        assert len(returned_object) == 6

        assert returned_object["active"] == False # noqa: E712
        assert returned_object["full_name"] == sample_server_data["full_name"]
        assert returned_object["symbol"] == sample_server_data["symbol"]
        assert returned_object["riot_symbol"] == sample_server_data["riot_symbol"]
        assert returned_object["hostname"] == sample_server_data["hostname"]

    def test_delete(self, mock_client, created_server):
        """
        DELETE test will remove the server object from the database.
        Additional GET check will test if resource was delete succesfully.
        """
        delete_response = mock_client.delete(f"/server/{created_server['id']}")
        assert delete_response.status_code == 200

        # We check if object with 'id' returned from previous DELETE does not exist anymore
        get_response = mock_client.get(f"/server/{delete_response.json()["id"]}")
        assert get_response.status_code == 404        