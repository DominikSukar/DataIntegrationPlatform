import pytest

from tests.setup import mock_client  # noqa: F401


@pytest.fixture(scope="class")
def sample_summoner_spell_data():
    "Sample fixture returns an examplary summoner spell data"
    return {
        "riot_id": 21,
        "name": "Barrier",
        "description": "Gain a 120-480 damage Shield for 2.5 seconds.",
    }


class TestSummonerSpellAPI:
    @pytest.fixture(scope="class")
    def created_summoner_spell(
        self, mock_client, sample_summoner_spell_data  # noqa: F811
    ):
        """
        Method uses POST to create summoner spell data based on a sample and returns the server's response.
        It is used in future tests:
        test_post - to check if returned data equals the one used to create an object
        test_get, test_patch, test_delete - to use returned 'id' attribute.
        """
        response = mock_client.post(
            "/summoner_spells/", json=sample_summoner_spell_data
        )
        assert response.status_code == 201

        return response.json()

    def test_post(self, sample_summoner_spell_data, created_summoner_spell):
        """
        Test only checks id data created by created_summoner_spell fixture does equal
        to data used to create an object.
        """

        # We check for 4 keys since 'id' should be returned as well (so 3+1 keys)
        assert len(created_summoner_spell) == 4

        assert created_summoner_spell["id"] == 1
        assert (
            created_summoner_spell["riot_id"] == sample_summoner_spell_data["riot_id"]
        )
        assert created_summoner_spell["name"] == sample_summoner_spell_data["name"]
        assert (
            created_summoner_spell["description"]
            == sample_summoner_spell_data["description"]
        )

    def test_list(self, mock_client, sample_summoner_spell_data):  # noqa: F811
        """
        List GET endpoint should return a list with only one object.
        Furthermore, we have to delete the 'id' key returned after creating object.
        """
        response = mock_client.get("/summoner_spells/")
        assert response.status_code == 200

        first_object = response.json()[0]
        # We check for 4 keys since 'id' should be returned as well (so 3+1 keys)
        assert len(first_object) == 4

        assert first_object["id"] == 1
        assert first_object["riot_id"] == sample_summoner_spell_data["riot_id"]
        assert first_object["name"] == sample_summoner_spell_data["name"]
        assert first_object["description"] == sample_summoner_spell_data["description"]

    def test_get(
        self,
        mock_client,  # noqa: F811
        sample_summoner_spell_data,
        created_summoner_spell,
    ):
        """
        GET endpoint returns specific object from the database
        """
        response = mock_client.get(f"/summoner_spells/{created_summoner_spell["id"]}")
        assert response.status_code == 200

        returned_object = response.json()
        # We check for 4 keys since 'id' should be returned as well (so 3+1 keys)
        assert len(returned_object) == 4

        assert returned_object["id"] == 1
        assert returned_object["riot_id"] == sample_summoner_spell_data["riot_id"]
        assert returned_object["name"] == sample_summoner_spell_data["name"]
        assert (
            returned_object["description"] == sample_summoner_spell_data["description"]
        )

    def test_patch(
        self,
        mock_client,  # noqa: F811
        created_summoner_spell,
        sample_summoner_spell_data,
    ):
        """
        PATCH test will update the 'active' attribute from 'True' to 'False'
        """
        update_data = {"active": False}
        response = mock_client.patch(
            f"/summoner_spells/{created_summoner_spell['id']}", json=update_data
        )
        assert response.status_code == 200

        returned_object = response.json()
        # We check for 4 keys since 'id' should be returned as well (so 3+1 keys)
        assert len(returned_object) == 4

        assert returned_object["id"] == 1
        assert returned_object["riot_id"] == sample_summoner_spell_data["riot_id"]
        assert returned_object["name"] == sample_summoner_spell_data["name"]
        assert (
            returned_object["description"] == sample_summoner_spell_data["description"]
        )

    def test_delete(self, mock_client, created_summoner_spell):  # noqa: F811
        """
        DELETE test will remove the server object from the database.
        Additional GET check will test if resource was delete succesfully.
        """
        delete_response = mock_client.delete(
            f"/summoner_spells/{created_summoner_spell['id']}"
        )
        assert delete_response.status_code == 200

        # We check if object with 'id' returned from previous DELETE does not exist anymore
        get_response = mock_client.get(
            f"/summoner_spells/{delete_response.json()["id"]}"
        )
        assert get_response.status_code == 404
