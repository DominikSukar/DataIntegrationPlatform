import pytest

from tests.setup import mock_client  # noqa: F401


@pytest.fixture(scope="class")
def sample_split_data():
    "Sample fixture returns an examplary split data"
    return {
        "name": "S1",
        "season_id": 1,
        "start_date": "2024-05-24 00:00:00",
        "end_date": "2024-09-24 23:59:59",
    }


class TestSplitAPI:
    @pytest.fixture(scope="class")
    def created_split(self, mock_client, sample_split_data):  # noqa: F811
        """
        Method uses POST to create split data based on a sample and returns the server's response.
        It is used in future tests:
        test_post - to check if returned data equals the one used to create an object
        test_get, test_patch, test_delete - to use returned 'id' attribute.
        """
        response = mock_client.post("/splits/", json=sample_split_data)
        assert response.status_code == 201

        return response.json()

    def test_post(self, sample_split_data, created_split):
        """
        Test only checks id data created by created_server fixture does equal
        to data used to create an object.
        """

        # We check for 5 keys since 'id' should be returned as well (so 4+1 keys)
        assert len(created_split) == 5

        assert created_split["id"] == 1
        assert created_split["name"] == sample_split_data["name"]
        assert created_split["start_date"] == sample_split_data["start_date"]
        assert created_split["end_date"] == sample_split_data["end_date"]

    def test_list(self, mock_client, sample_split_data):  # noqa: F811
        """
        List GET endpoint should return a list with only one object.
        Furthermore, we have to delete the 'id' key returned after creating object.
        """
        response = mock_client.get("/splits/")
        assert response.status_code == 200

        first_object = response.json()[0]
        # We check for 5 keys since 'id' should be returned as well (so 4+1 keys)
        assert len(first_object) == 5

        assert first_object["id"] == 1
        assert first_object["name"] == sample_split_data["name"]
        assert first_object["start_date"] == sample_split_data["start_date"]
        assert first_object["end_date"] == sample_split_data["end_date"]

    def test_get(self, mock_client, sample_split_data, created_split):  # noqa: F811
        """
        GET endpoint returns specific object from the database
        """
        response = mock_client.get(f"/splits/{created_split["id"]}")
        assert response.status_code == 200

        returned_object = response.json()
        # We check for 5 keys since 'id' should be returned as well (so 4+1 keys)
        assert len(returned_object) == 5

        assert returned_object["id"] == 1
        assert returned_object["name"] == sample_split_data["name"]
        assert returned_object["start_date"] == sample_split_data["start_date"]
        assert returned_object["end_date"] == sample_split_data["end_date"]

    def test_patch(self, mock_client, created_split, sample_split_data):  # noqa: F811
        """
        PATCH test will update the 'name' attribute from from 'S1' to 'S2'
        """
        update_data = {"name": "S2"}
        response = mock_client.patch(f"/splits/{created_split['id']}", json=update_data)
        assert response.status_code == 200

        returned_object = response.json()
        # We check for 5 keys since 'id' should be returned as well (so 4+1 keys)
        assert len(returned_object) == 5

        assert returned_object["id"] == 1
        assert returned_object["name"] == update_data["name"]
        assert returned_object["start_date"] == sample_split_data["start_date"]
        assert returned_object["end_date"] == sample_split_data["end_date"]

    def test_delete(self, mock_client, created_split):  # noqa: F811
        """
        DELETE test will remove the server object from the database.
        Additional GET check will test if resource was delete succesfully.
        """
        delete_response = mock_client.delete(f"/splits/{created_split['id']}")
        assert delete_response.status_code == 200

        # We check if object with 'id' returned from previous DELETE does not exist anymore
        get_response = mock_client.get(f"/splits/{delete_response.json()["id"]}")
        assert get_response.status_code == 404
