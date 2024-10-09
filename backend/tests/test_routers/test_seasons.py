import pytest

from tests.setup import mock_client  # noqa: F401


@pytest.fixture(scope="class")
def sample_season_data():
    "Sample fixture returns an examplary season data"
    return {
        "name": "S2024",
        "start_date": "2024-05-24 00:00:00",
        "end_date": "2024-09-24 23:59:59",
    }


class TestSeasonAPI:
    @pytest.fixture(scope="class")
    def created_season(self, mock_client, sample_season_data):  # noqa: F811
        """
        Method uses POST to create season data based on a sample and returns the server's response.
        It is used in future tests:
        test_post - to check if returned data equals the one used to create an object
        test_get, test_patch, test_delete - to use returned 'id' attribute.
        """
        response = mock_client.post("/seasons/", json=sample_season_data)
        assert response.status_code == 201

        return response.json()

    def test_post(self, sample_season_data, created_season):
        """
        Test only checks id data created by created_server fixture does equal
        to data used to create an object.
        """

        # We check for 4 keys since 'id' should be returned as well (so 3+1 keys)
        assert len(created_season) == 4

        assert created_season["id"] == 1
        assert created_season["name"] == sample_season_data["name"]
        assert created_season["start_date"] == sample_season_data["start_date"]
        assert created_season["end_date"] == sample_season_data["end_date"]

    def test_list(self, mock_client, sample_season_data):  # noqa: F811
        """
        List GET endpoint should return a list with only one object.
        Furthermore, we have to delete the 'id' key returned after creating object.
        """
        response = mock_client.get("/seasons/")
        assert response.status_code == 200

        first_object = response.json()[0]
        # We check for 4 keys since 'id' should be returned as well (so 3+1 keys)
        assert len(first_object) == 4

        assert first_object["id"] == 1
        assert first_object["name"] == sample_season_data["name"]
        assert first_object["start_date"] == sample_season_data["start_date"]
        assert first_object["end_date"] == sample_season_data["end_date"]

    def test_get(self, mock_client, sample_season_data, created_season):  # noqa: F811
        """
        GET endpoint returns specific object from the database
        """
        response = mock_client.get(f"/seasons/{created_season["id"]}")
        assert response.status_code == 200

        returned_object = response.json()
        # We check for 4 keys since 'id' should be returned as well (so 3+1 keys)
        assert len(returned_object) == 4

        assert returned_object["id"] == 1
        assert returned_object["name"] == sample_season_data["name"]
        assert returned_object["start_date"] == sample_season_data["start_date"]
        assert returned_object["end_date"] == sample_season_data["end_date"]

    def test_patch(self, mock_client, created_season, sample_season_data):  # noqa: F811
        """
        PATCH test will update the 'name' attribute from from 'S2024' to 'S2025'
        """
        update_data = {"name": "S2025"}
        response = mock_client.patch(
            f"/seasons/{created_season['id']}", json=update_data
        )
        assert response.status_code == 200

        returned_object = response.json()
        # We check for 5 keys since 'id' should be returned as well (so 4+1 keys)
        assert len(returned_object) == 4

        assert returned_object["id"] == 1
        assert returned_object["name"] == update_data["name"]
        assert returned_object["start_date"] == sample_season_data["start_date"]
        assert returned_object["end_date"] == sample_season_data["end_date"]

    def test_delete(self, mock_client, created_season):  # noqa: F811
        """
        DELETE test will remove the server object from the database.
        Additional GET check will test if resource was delete succesfully.
        """
        delete_response = mock_client.delete(f"/seasons/{created_season['id']}")
        assert delete_response.status_code == 200

        # We check if object with 'id' returned from previous DELETE does not exist anymore
        get_response = mock_client.get(f"/seasons/{delete_response.json()["id"]}")
        assert get_response.status_code == 404
