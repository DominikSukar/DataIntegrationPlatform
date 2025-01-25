import pytest


@pytest.fixture(scope="class")
def sample_user_data():
    "Sample fixture returns an examplary user data"
    return {
        "gameName": "PrinceOfEssling",
        "tagLine": "EUW",
        "puuid": "fEqAg32w5pgve-Z_XpBI5K9TU9e8nsWQUCfyoYf1YooGT97WqTVplDSeKB3qx0amhd2tW0lLGq1SjQ",
    }


@pytest.fixture(scope="class")
def sample_summoner_data():
    "Sample fixture returns an examplary summoner data based on SUMMONER-V4 api"
    return {
        "id": "AsRbuunzS_WO5N-x3cz4nzp7I07ARKRGc_ggnk80ogmXuVA",
        "accountId": "rkx2e4GlYoIXSUv8pNrLOGE0BlHodPGnH4bRf_G5V7dDaQc",
        "puuid": "fEqAg32w5pgve-Z_XpBI5K9TU9e8nsWQUCfyoYf1YooGT97WqTVplDSeKB3qx0amhd2tW0lLGq1SjQ",
        "profileIconId": 1230,
        "revisionDate": 1724699243000,
        "summonerLevel": 82,
    }
