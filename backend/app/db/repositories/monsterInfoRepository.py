from app.db.session import session_scope
from app.db.models.monsterInfo import MonsterInfo
from .repository import Repository


class MonsterInfoRepository(Repository):
    def __init__(self):
        super().__init__(MonsterInfo)

    def get_by_id(self, id: int) -> MonsterInfo:
        with session_scope() as session:
            return session.query(self.entityClass).filter_by(id=id).first()
