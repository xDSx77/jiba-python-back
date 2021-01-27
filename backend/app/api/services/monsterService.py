from typing import List

from app.db.models.monsterInfo import MonsterInfo
from app.db.repositories.monsterInfoRepository import MonsterInfoRepository

class MonsterService:

    def __init__(self):
        self.monster_info_repository = MonsterInfoRepository()

    def get_all(self) -> List[MonsterInfo]:
        return self.monster_info_repository.get_all()

    def get_monster_info(self, monster_id: int) -> MonsterInfo:
        return self.monster_repository.get_by_monster_id(monster_id)
