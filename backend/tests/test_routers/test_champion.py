import pytest

from tests.setup import mock_client  # noqa: F401


@pytest.fixture(scope="class")
def sample_champion_data():
    "Sample fixture returns an examplary champion data"
    return {"riot_id": 266, "name": "Aatrox"}


class TestChampionPI:
    @pytest.fixture(scope="class")
    def created_champion(self, mock_client, sample_champion_data):  # noqa: F811
        """
        Method uses POST to create champion data based on a sample and returns the server's response.
        It is used in future tests:
        test_post - to check if returned data equals the one used to create an object
        test_get, test_patch, test_delete - to use returned 'id' attribute.
        """
        response = mock_client.post("/champions/", json=sample_champion_data)
        assert response.status_code == 201

        return response.json()

    def test_post(self, sample_champion_data, created_champion):
        """
        Test only checks id data created by created_champion fixture does equal
        to data used to create an object.
        """

        # We check for 3 keys since 'id' should be returned as well (so 2+1 keys)
        assert len(created_champion) == 3

        assert created_champion["id"] == 1
        assert created_champion["riot_id"] == sample_champion_data["riot_id"]
        assert created_champion["name"] == sample_champion_data["name"]

    def test_list(self, mock_client, sample_champion_data):  # noqa: F811
        """
        List GET endpoint should return a list with only one object.
        Furthermore, we have to delete the 'id' key returned after creating object.
        """
        response = mock_client.get("/champions/")
        assert response.status_code == 200

        first_object = response.json()[0]
        # We check for 3 keys since 'id' should be returned as well (so 2+1 keys)
        assert len(first_object) == 3

        assert first_object["id"] == 1
        assert first_object["riot_id"] == sample_champion_data["riot_id"]
        assert first_object["name"] == sample_champion_data["name"]

    def test_list_query_riot_id(self, mock_client, sample_champion_data):  # noqa: F811
        """
        This test additionally checks if filtering by riot_id is supported
        """
        response = mock_client.get(
            f"/champions/?riot_id={sample_champion_data['riot_id']}"
        )
        assert response.status_code == 200

        first_object = response.json()[0]
        # We check for 3 keys since 'id' should be returned as well (so 2+1 keys)
        assert len(first_object) == 3

        assert first_object["id"] == 1
        assert first_object["riot_id"] == sample_champion_data["riot_id"]
        assert first_object["name"] == sample_champion_data["name"]

        # In theory this riot_id should not exist and endpoint should correctly respond with empty list
        response = mock_client.get("/champions/?riot_id=99999")
        assert response.status_code == 200

        first_object = response.json()

        assert len(first_object) == 0

    def test_list_query_name(self, mock_client, sample_champion_data):  # noqa: F811
        """
        This test additionally checks if filtering by name and name is supported
        """
        response = mock_client.get(f"/champions/?name={sample_champion_data['name']}")
        assert response.status_code == 200

        first_object = response.json()[0]
        # We check for 3 keys since 'id' should be returned as well (so 2+1 keys)
        assert len(first_object) == 3

        assert first_object["id"] == 1
        assert first_object["riot_id"] == sample_champion_data["riot_id"]
        assert first_object["name"] == sample_champion_data["name"]

        # 'Liandry' is an item name to should not exist in perks table
        response = mock_client.get("/champions/?name=Liandry")
        assert response.status_code == 200

        first_object = response.json()

        assert len(first_object) == 0

    def test_get(
        self, mock_client, sample_champion_data, created_champion  # noqa: F811
    ):
        """
        GET endpoint returns specific object from the database
        """
        response = mock_client.get(f"/champions/{created_champion["id"]}")
        assert response.status_code == 200

        returned_object = response.json()
        # We check for 3 keys since 'id' should be returned as well (so 2+1 keys)
        assert len(returned_object) == 3

        assert returned_object["id"] == 1
        assert returned_object["riot_id"] == sample_champion_data["riot_id"]
        assert returned_object["name"] == sample_champion_data["name"]

    def test_patch(
        self, mock_client, created_champion, sample_champion_data  # noqa: F811
    ):
        """
        PATCH test will update the 'active' attribute from 'True' to 'False'
        """
        update_data = {"active": False}
        response = mock_client.patch(
            f"/champions/{created_champion['id']}", json=update_data
        )
        assert response.status_code == 200

        returned_object = response.json()
        # We check for 3 keys since 'id' should be returned as well (so 2+1 keys)
        assert len(returned_object) == 3

        assert returned_object["id"] == 1
        assert returned_object["riot_id"] == sample_champion_data["riot_id"]
        assert returned_object["name"] == sample_champion_data["name"]

    def test_delete(self, mock_client, created_champion):  # noqa: F811
        """
        DELETE test will remove the server object from the database.
        Additional GET check will test if resource was delete succesfully.
        """
        delete_response = mock_client.delete(f"/champions/{created_champion['id']}")
        assert delete_response.status_code == 200

        # We check if object with 'id' returned from previous DELETE does not exist anymore
        get_response = mock_client.get(f"/champions/{delete_response.json()["id"]}")
        assert get_response.status_code == 404
