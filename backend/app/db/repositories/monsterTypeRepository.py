from app.db.session import session_scope
from app.api.models.monsterType import MonsterType
from app.db.repositories.repository import Repository


class MonsterTypeRepository(Repository):
    def __init__(self):
        super().__init__(MonsterType)

    def get_by_id(self, id: int):
        with session_scope() as session:
            return session.query(self.entityClass).filter_by(id=id).first()