import json

import pytest
import requests

API_URL = "http://localhost:8000/api"


@pytest.fixture()
def create_player_url():
    return API_URL + "/players/create"


@pytest.fixture()
def get_players_url():
    return API_URL + "/players/"


@pytest.fixture()
def get_player_info_url():
    return API_URL + "/players/info/test_username"


def test_create_player(create_player_url):
    response = requests.post(create_player_url, data=json.dumps({"username": "test_username"}), headers={'Content-Type': 'application/json'})
    response_body = response.json()
    assert response_body["message"] == "A new hero has appeared: test_username."
    response = requests.post(create_player_url, data=json.dumps({"username": "test_username"}), headers={'Content-Type': 'application/json'})
    response_body = response.json()
    assert response_body["message"] == "This hero already exists, find another username."


def test_get_players(get_players_url):
    response = requests.get(get_players_url)
    response_body = response.json()
    assert response_body["message"] == "There are 1 heroes in this world."
    assert len(response_body["heroes"]) == 1
    assert response_body["heroes"][0] == "test_username (level 1)"


def test_player_info(get_player_info_url):
    response = requests.get(get_player_info_url)
    response_body = response.json()
    assert response_body["message"] == "test_username is a level 1 hero (0/100xp). He is broke. He feels good."
