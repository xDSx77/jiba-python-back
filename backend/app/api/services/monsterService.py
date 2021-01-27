from typing import List

from app.db.models.monster import Monster
from app.db.repositories import MonsterRepository
from app.db.repositories import MonsterTypeRepository


class MonsterService:

    def __init__(self):
        self.monster_repository = MonsterRepository()
        self.monster_type_repository = MonsterTypeRepository()

    def get_all(self) -> List[Monster]:
        return self.monster_repository.get_all()

    def get_monster_info(self, monster_id: int) -> Monster:
        return self.monster_repository.get_by_monster_id(monster_id)
