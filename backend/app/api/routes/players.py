from typing import List

from fastapi import APIRouter
from pydantic import BaseModel

from app.api.models.player import Player
from app.api.services import PlayerService


class CreatePlayerRequest(BaseModel):
    pass


router = APIRouter()


@router.get("/")
async def get_all_players() -> List[Player]:
    playerService = PlayerService()
    return playerService.get_all_players()


@router.post("/create")
async def create_new_player(create_player_request: CreatePlayerRequest) -> Player:
    playerService = PlayerService()
    return playerService.create_new_player(create_player_request)


@router.get("/info/{username}")
async def get_player_info(username: str) -> Player:
    playerService = PlayerService()
    return playerService.get_player_info(username)


@router.get("/rest/{username}")
async def rest(username: str) -> Player:
    playerService = PlayerService()
    return playerService.rest(username)


@router.get("/{username}/attack/{monster_id}/")
async def attack(username: str, monster_id: int) -> object:
    playerService = PlayerService()
    return playerService.attack(username, monster_id)
