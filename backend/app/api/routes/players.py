from fastapi import APIRouter
from pydantic import BaseModel

from app.db.models.player import Player
from app.api.services import PlayerService


class CreatePlayerRequest(BaseModel):
    username: str


router = APIRouter()


@router.get("/")
async def get_all_players():
    playerService = PlayerService()
    heroes = playerService.get_all_players()
    message = f"There are {len(heroes)} heroes in this world."
    heroes_list = [f"{hero.username} (level {hero.level})" for hero in heroes]
    return {
        "message": message,
        "heroes": heroes_list
    }

@router.post("/create")
async def create_new_player(create_player_request: CreatePlayerRequest):
    playerService = PlayerService()
    new_player = playerService.create_new_player(create_player_request.username)
    if new_player is None:
        return {
            "message": "This hero already exists, find another username.",
        }
    return {
        "message": f"A new hero has appeared: {new_player.username}.",
    }


@router.get("/info/{username}")
async def get_player_info(username: str) -> Player:
    playerService = PlayerService()
    player = playerService.get_player_info(username)
    if player is None:
        return {"message": "Player does not exist"}

    health_message = "He feels good."
    health_ratio = float(player.hp) / float(player.hp_max)
    if 0.4 <= health_ratio < 0.7:
        health_message = "He could need some rest."
    elif health_ratio < 0.4:
        health_message = "He is seriously injured."
    money_message = "He is broke." if player.gold == 0 else f"He has {player.gold} coin(s) in his purse."

    return {
        "message": f"{username} is a level {player.level} hero ({player.xp}/{player.xp_max}xp). "
        + money_message + " " + health_message
    }


@router.post("/rest/{username}")
async def rest(username: str):
    playerService = PlayerService()
    player = playerService.rest(username)
    return {
        "message": f"Tired, {player.username} sat near the fire and took a nap (hp {player.hp}/{player.hp_max})."
    }


@router.post("/{username}/attack/{monster_id}/")
async def attack(username: str, monster_id: int) -> object:
    playerService = PlayerService()
    attack = playerService.attack(username, monster_id)
    message = ""
    monster_info = attack["monster_info"]
    leveled_up = attack["levelUp"]
    if attack["player_died"]:
        message = f"{username} died fighting the terrible creature. Luckily a wizard found him and revived him, however it costed him half his purse."
    elif attack["monster_died"]:
        message = f"{username} killed the creature and found {monster_info.gold_value} gold coins on its remains(+{monster_info.xp}xp)." + "The hero level up!" if leveled_up else ""
    else:
        message = f"{username} attacked the creature but it fought back(-{monster_info.damage}hp)."
    return {
        "message": message
    }
