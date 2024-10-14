import pytest

from tests.setup import mock_client  # noqa: F401


@pytest.fixture(scope="class")
def sample_perk_data():
    "Sample fixture returns an examplary perk data"
    return {
        "riot_id": 1001,
        "name": "Boots",
        "description": "<mainText><stats><attention>25</attention> Move Speed</stats><br><br></mainText>",
    }


class TestPerkAPI:
    @pytest.fixture(scope="class")
    def created_perk(self, mock_client, sample_perk_data):  # noqa: F811
        """
        Method uses POST to create perk data based on a sample and returns the server's response.
        It is used in future tests:
        test_post - to check if returned data equals the one used to create an object
        test_get, test_patch, test_delete - to use returned 'id' attribute.
        """
        response = mock_client.post("/perks/", json=sample_perk_data)
        assert response.status_code == 201

        return response.json()

    def test_post(self, sample_perk_data, created_perk):
        """
        Test only checks id data created by created_perk fixture does equal
        to data used to create an object.
        """

        # We check for 4 keys since 'id' should be returned as well (so 3+1 keys)
        assert len(created_perk) == 4

        assert created_perk["id"] == 1
        assert created_perk["riot_id"] == sample_perk_data["riot_id"]
        assert created_perk["name"] == sample_perk_data["name"]
        assert created_perk["description"] == sample_perk_data["description"]

    def test_list(self, mock_client, sample_perk_data):  # noqa: F811
        """
        List GET endpoint should return a list with only one object.
        Furthermore, we have to delete the 'id' key returned after creating object.
        """
        response = mock_client.get("/perks/")
        assert response.status_code == 200

        first_object = response.json()[0]
        # We check for 4 keys since 'id' should be returned as well (so 3+1 keys)
        assert len(first_object) == 4

        assert first_object["id"] == 1
        assert first_object["riot_id"] == sample_perk_data["riot_id"]
        assert first_object["name"] == sample_perk_data["name"]
        assert first_object["description"] == sample_perk_data["description"]

    def test_list_query_riot_id(self, mock_client, sample_perk_data):  # noqa: F811
        """
        This test additionally checks if filtering by riot_id is supported
        """
        response = mock_client.get(f"/perks/?riot_id={sample_perk_data['riot_id']}")
        assert response.status_code == 200

        first_object = response.json()[0]
        # We check for 4 keys since 'id' should be returned as well (so 3+1 keys)
        assert len(first_object) == 4

        assert first_object["id"] == 1
        assert first_object["riot_id"] == sample_perk_data["riot_id"]
        assert first_object["name"] == sample_perk_data["name"]
        assert first_object["description"] == sample_perk_data["description"]

        # In theory this riot_id should not exist and endpoint should correctly respond with empty list
        response = mock_client.get("/perks/?riot_id=99999")
        assert response.status_code == 200

        first_object = response.json()

        assert len(first_object) == 0

    def test_list_query_name(self, mock_client, sample_perk_data):  # noqa: F811
        """
        This test additionally checks if filtering by name and name is supported
        """
        response = mock_client.get(f"/perks/?name={sample_perk_data['name']}")
        assert response.status_code == 200

        first_object = response.json()[0]
        # We check for 4 keys since 'id' should be returned as well (so 3+1 keys)
        assert len(first_object) == 4

        assert first_object["id"] == 1
        assert first_object["riot_id"] == sample_perk_data["riot_id"]
        assert first_object["name"] == sample_perk_data["name"]
        assert first_object["description"] == sample_perk_data["description"]

        # 'Linadry' is an item name to should not exist in perks table
        response = mock_client.get("/perks/?name=Liandry")
        assert response.status_code == 200

        first_object = response.json()

        assert len(first_object) == 0

    def test_get(self, mock_client, sample_perk_data, created_perk):  # noqa: F811
        """
        GET endpoint returns specific object from the database
        """
        response = mock_client.get(f"/perks/{created_perk["id"]}")
        assert response.status_code == 200

        returned_object = response.json()
        # We check for 4 keys since 'id' should be returned as well (so 3+1 keys)
        assert len(created_perk) == 4

        assert returned_object["id"] == 1
        assert returned_object["riot_id"] == sample_perk_data["riot_id"]
        assert returned_object["name"] == sample_perk_data["name"]
        assert returned_object["description"] == sample_perk_data["description"]

    def test_patch(self, mock_client, created_perk, sample_perk_data):  # noqa: F811
        """
        PATCH test will update the 'active' attribute from 'True' to 'False'
        """
        update_data = {"active": False}
        response = mock_client.patch(f"/perks/{created_perk['id']}", json=update_data)
        assert response.status_code == 200

        returned_object = response.json()
        # We check for 4 keys since 'id' should be returned as well (so 3+1 keys)
        assert len(created_perk) == 4

        assert returned_object["id"] == 1
        assert returned_object["riot_id"] == sample_perk_data["riot_id"]
        assert returned_object["name"] == sample_perk_data["name"]
        assert returned_object["description"] == sample_perk_data["description"]

    def test_delete(self, mock_client, created_perk):  # noqa: F811
        """
        DELETE test will remove the server object from the database.
        Additional GET check will test if resource was delete succesfully.
        """
        delete_response = mock_client.delete(f"/perks/{created_perk['id']}")
        assert delete_response.status_code == 200

        # We check if object with 'id' returned from previous DELETE does not exist anymore
        get_response = mock_client.get(f"/perks/{delete_response.json()["id"]}")
        assert get_response.status_code == 404
