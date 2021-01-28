import json

import pytest
import requests

API_URL = "http://localhost:8000/api"
MONSTER_ROUTE = "/monsters"

@pytest.fixture()
def get_monsters_url():
    return API_URL + MONSTER_ROUTE + "/"


@pytest.fixture()
def get_monster_info_url():
    return API_URL + MONSTER_ROUTE + "/info/"


def test_get_all_monsters(get_monsters_url):
    response = requests.get(get_monsters_url, headers={'Content-Type': 'application/json'})
    response_body = response.json()
    assert response_body["message"] == "The world contains 8 monsters"
    assert response_body["monsters"] == [
        "rat (id: 1) 3/3 HP",
        "rat (id: 2) 3/3 HP",
        "rat (id: 3) 3/3 HP",
        "spider (id: 4) 4/4 HP",
        "spider (id: 5) 4/4 HP",
        "wolf (id: 6) 7/7 HP",
        "dragon (id: 7) 50/50 HP",
        "chicken (id: 8) 5/5 HP"
    ]

def test_get_monster_info(get_monster_info_url):
    response = requests.get(get_monster_info_url + "1", headers={'Content-Type': 'application/json'})
    response_body = response.json()
    assert response_body["message"] == "rat (id: 1) 3/3 HP. rat does 1 damage. Upon death, its rewarded by 1 golds and 3 experience points"


def test_get_fake_monster_info(get_monster_info_url):
    response = requests.get(get_monster_info_url + "100", headers={'Content-Type': 'application/json'})
    response_body = response.json()
    assert response_body["message"] == "There is now monster with id: 100"