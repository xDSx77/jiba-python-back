from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter()


@router.get("/")
async def get_all_monsters() -> object:
    return None


@router.get("/info/{monster_id}")
async def get_monster_info(monster_id: int) -> object:
    return None
