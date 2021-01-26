from app.db.session import session_scope
from app.api.models.monster import Monster
from app.db.repositories.repository import Repository


class MonsterRepository(Repository):
    def __init__(self):
        super().__init__(Monster)

    def get_by_monster_id(self, id: int):
        with session_scope() as session:
            return session.query(self.entityClass).filter_by(id=id).first()