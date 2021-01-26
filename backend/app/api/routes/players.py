from fastapi import APIRouter
from pydantic import BaseModel


class CreatePlayerRequest(BaseModel):
    pass


router = APIRouter()


@router.get("/")
async def get_all_players() -> object:
    return None


@router.post("/create")
async def create_new_player(create_player_request: CreatePlayerRequest) -> object:
    return None


@router.get("/info/{username}")
async def get_player_info(username: str) -> object:
    return None


@router.get("/rest/{username}")
async def rest(username: str) -> object:
    return None


@router.get("/attack/{monster_id}")
async def attack(monster_id: int) -> object:
    return None
