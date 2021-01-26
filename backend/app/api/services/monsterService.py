from app.db.repositories.monsterRepository import MonsterRepository
from app.db.repositories.monsterTypeRepository import MonsterTypeRepository

class MonsterService:

    def __init__(self):
        self.monster_repository = MonsterRepository()
        self.monster_type_repository = MonsterTypeRepository()

    def get_all(self):
        return self.monster_repository.get_all()

    def get_monster_info(self, monster_id: int):
        pass
