import json

import pytest
import requests

API_URL = "http://localhost:8000/api/"


@pytest.fixture()
def create_player_url():
    return API_URL + "players/create"


def test_create_player(create_player_url):
    response = requests.post(create_player_url, data=json.dumps({"username": "test_username"}), headers={'Content-Type': 'application/json'})
    assert response.text == "A new hero has appeared: test_username"
