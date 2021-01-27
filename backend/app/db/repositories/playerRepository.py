from app.db.session import session_scope
from .repository import Repository
from app.db.models.player import Player


class PlayerRepository(Repository):
    def __init__(self):
        super().__init__(Player)

    def get_by_username(self, username) -> Player:
        with session_scope() as session:
            return session.query(self.entityClass).filter_by(username=username).first()

    def update_by_username(self, entity: Player):
        with session_scope() as session:
            fields_to_update = {
                "hp": entity.hp,
                "xp": entity.xp,
                "level": entity.level,
                "gold": entity.gold
            }
            return session.query(self.entityClass)\
                .filter_by(username=entity.username)\
                .update(fields_to_update)
