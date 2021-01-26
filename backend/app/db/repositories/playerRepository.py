from app.db.session import session_scope
from .repository import Repository
from app.db.models.player import Player


class PlayerRepository(Repository):
    def __init__(self):
        super().__init__(Player)

    def get_by_player_name(self, username):
        with session_scope() as session:
            return session.query(self.entityClass).filter_by(username=username).first()
