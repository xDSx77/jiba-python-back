from typing import List

from app.db.models.player import Player
from app.api.routes.players import CreatePlayerRequest
from app.db.repositories import PlayerRepository


class PlayerService:

    def __init__(self):
        self.player_repository = PlayerRepository()

    def get_all_players(self) -> List[Player]:
        pass

    def create_new_player(self, create_player_request : CreatePlayerRequest) -> Player:
        pass

    def get_player_info(self, username: str) -> Player:
        pass

    def rest(self, username: str) -> Player:
        pass

    def attack(self, username: str, monster_id: int) -> object:
        pass
