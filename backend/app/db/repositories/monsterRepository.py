from app.db.session import session_scope
from app.db.models.monster import Monster
from .repository import Repository


class MonsterRepository(Repository):
    def __init__(self):
        super().__init__(Monster)

    def get_by_monster_id(self, id: int) -> Monster:
        with session_scope() as session:
            return session.query(self.entityClass).filter_by(id=id).first()

    def update_by_id(self, entity: Monster):
        with session_scope() as session:
            fields_to_update = {
                "hp": entity.hp,
            }
            return session.query(Monster)\
                .filter_by(id=entity.id)\
                .update(fields_to_update)

    def delete_by_id(self, id: int):
        with session_scope() as session:
            monster = self.get_by_monster_id(id)
            session.delete(monster)
