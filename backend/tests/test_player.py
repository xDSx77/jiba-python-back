import json

import pytest
import requests

API_URL = "http://localhost:8000/api"
TEST_USERNAME = "test_username"

@pytest.fixture()
def create_player_url():
    return f"{API_URL}/players/create"


@pytest.fixture()
def get_players_url():
    return f"{API_URL}/players/"


@pytest.fixture()
def get_player_info_url():
    return f"{API_URL}/players/info/{TEST_USERNAME}"


@pytest.fixture()
def attack_monster_one_url():
    return f"{API_URL}/players/{TEST_USERNAME}/attack/1"


@pytest.fixture()
def attack_monster_four_url():
    return f"{API_URL}/players/{TEST_USERNAME}/attack/4"


@pytest.fixture()
def attack_monster_seven_url():
    return f"{API_URL}/players/{TEST_USERNAME}/attack/7"


@pytest.fixture()
def attack_monster_eight_url():
    return f"{API_URL}/players/{TEST_USERNAME}/attack/8"


@pytest.fixture()
def rest_url():
    return f"{API_URL}/players/rest/{TEST_USERNAME}"


@pytest.fixture()
def attack_unknown_player_url():
    return f"{API_URL}/players/UNKNOWN/attack/2"


@pytest.fixture()
def attack_unknown_monster_url():
    return f"{API_URL}/players/{TEST_USERNAME}/attack/50"


def test_create_player(create_player_url):
    response = requests.post(create_player_url, data=json.dumps({"username": TEST_USERNAME}), headers={'Content-Type': 'application/json'})
    response_body = response.json()
    assert response_body["message"] == f"A new hero has appeared: {TEST_USERNAME}."


def test_create_player_already_exists(create_player_url):
    response = requests.post(create_player_url, data=json.dumps({"username": TEST_USERNAME}), headers={'Content-Type': 'application/json'})
    response_body = response.json()
    assert response_body["message"] == "This hero already exists, find another username."


def test_get_players(get_players_url):
    response = requests.get(get_players_url)
    response_body = response.json()
    assert response_body["message"] == "There are 1 heroes in this world."
    assert len(response_body["heroes"]) == 1
    assert response_body["heroes"][0] == f"{TEST_USERNAME} (level 1)"


def test_player_info(get_player_info_url):
    response = requests.get(get_player_info_url)
    response_body = response.json()
    assert response_body["message"] == f"{TEST_USERNAME} is a level 1 hero (0/100xp). He is broke. He feels good."


def test_attack(attack_monster_one_url):
    response = requests.post(attack_monster_one_url, headers={'Content-Type': 'application/json'})
    response_body = response.json()
    assert response_body["message"] == f"{TEST_USERNAME} attacked the creature but it fought back(-1hp)."


def test_attack_and_kill(attack_monster_four_url):
    response = requests.post(attack_monster_four_url, headers={'Content-Type': 'application/json'})
    response_body = response.json()
    assert response_body["message"] == f"{TEST_USERNAME} attacked the creature but it fought back(-2hp)."
    response = requests.post(attack_monster_four_url, headers={'Content-Type': 'application/json'})
    response_body = response.json()
    assert response_body["message"] == f"{TEST_USERNAME} attacked the creature but it fought back(-2hp)."
    response = requests.post(attack_monster_four_url, headers={'Content-Type': 'application/json'})
    response_body = response.json()
    assert response_body["message"] == f"{TEST_USERNAME} attacked the creature but it fought back(-2hp)."
    response = requests.post(attack_monster_four_url, headers={'Content-Type': 'application/json'})
    response_body = response.json()
    assert response_body["message"] == f"{TEST_USERNAME} killed the creature and found 2 gold coins on its remains(+4xp)."


def test_rest(rest_url):
    response = requests.post(rest_url, headers={'Content-Type': 'application/json'})
    response_body = response.json()
    assert response_body["message"] == f"Tired, {TEST_USERNAME} sat near the fire and took a nap (hp 6/10)."


def test_attack_and_die(attack_monster_seven_url):
    response = requests.post(attack_monster_seven_url, headers={'Content-Type': 'application/json'})
    response_body = response.json()
    assert response_body["message"] == f"{TEST_USERNAME} died fighting the terrible creature. Luckily a wizard found him and revived him, however it cost him half his purse."


def test_attack_and_gain_level(attack_monster_eight_url):
    response = requests.post(attack_monster_eight_url, headers={'Content-Type': 'application/json'})
    response_body = response.json()
    assert response_body["message"] == f"{TEST_USERNAME} attacked the creature but it fought back(-0hp)."
    response = requests.post(attack_monster_eight_url, headers={'Content-Type': 'application/json'})
    response_body = response.json()
    assert response_body["message"] == f"{TEST_USERNAME} attacked the creature but it fought back(-0hp)."
    response = requests.post(attack_monster_eight_url, headers={'Content-Type': 'application/json'})
    response_body = response.json()
    assert response_body["message"] == f"{TEST_USERNAME} attacked the creature but it fought back(-0hp)."
    response = requests.post(attack_monster_eight_url, headers={'Content-Type': 'application/json'})
    response_body = response.json()
    assert response_body["message"] == f"{TEST_USERNAME} attacked the creature but it fought back(-0hp)."
    response = requests.post(attack_monster_eight_url, headers={'Content-Type': 'application/json'})
    response_body = response.json()
    assert response_body["message"] == f"{TEST_USERNAME} killed the creature and found 2 gold coins on its remains(+100xp). The hero leveled up!"


def test_attack_unknown_player(attack_unknown_player_url):
    response = requests.post(attack_unknown_player_url, headers={'Content-Type': 'application/json'})
    response_body = response.json()
    assert response_body["message"] == f"I swear i've never seen a hero going by this name."


def test_attack_unknown_monster(attack_unknown_monster_url):
    response = requests.post(attack_unknown_monster_url, headers={'Content-Type': 'application/json'})
    response_body = response.json()
    assert response_body["message"] == f"{TEST_USERNAME} kept looking for the creature but it was like it never existed."
