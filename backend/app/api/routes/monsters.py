from fastapi import APIRouter
from pydantic import BaseModel
from app.api.services.monsterService import MonsterService
from app.db.models.monster import Monster

router = APIRouter()


@router.get("/")
async def get_all_monsters() -> list[Monster]:
    return MonsterService().get_all()


@router.get("/info/{monster_id}")
async def get_monster_info(monster_id: int) -> object:
    return MonsterService().get_monster_info(monster_id)
