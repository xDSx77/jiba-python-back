from typing import Dict

from fastapi import APIRouter
from app.api.services.monsterService import MonsterService

router = APIRouter()


@router.get("/")
async def get_all_monsters():
    monster_infos = MonsterService().get_all()
    message = f"The world contains {len(monster_infos)} monsters"
    monster_messages = [f"{monster.name} (id: {monster.id}) {monster.hp}/{monster.hp_max} HP" for monster in monster_infos]
    return {
        "message": message,
        "monsters": monster_messages
    }


@router.get("/info/{monster_id}")
async def get_monster_info(monster_id: int) -> Dict[str, str]:
    monster_info = MonsterService().get_monster_info(monster_id)
    if monster_info is None:
        return {
            "message": f"There is now monster with id: {monster_id}"
        }

    return {
        "message": f"{monster_info.name} (id: {monster_info.id}) {monster_info.hp}/{monster_info.hp_max} HP. {monster_info.name} does {monster_info.damage} damage. Upon death, its rewarded by {monster_info.gold_value} golds and {monster_info.xp_value} experience points"
    }

