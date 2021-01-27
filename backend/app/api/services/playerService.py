from typing import List
from app.db.models.player import Player
from app.db.repositories import PlayerRepository


class PlayerService:

    def __init__(self):
        self.player_repository = PlayerRepository()

    def get_all_players(self) -> List[Player]:
        return self.player_repository.get_all()

    def create_new_player(self, username: str) -> Player:
        new_player = None
        if self.player_repository.get_by_username(username) is None:
            new_player = Player(username=username)
            self.save(new_player)
        return new_player

    def get_player_info(self, username: str) -> Player:
        return self.player_repository.get_by_username(username)

    def rest(self, username: str) -> Player:
        pass

    def attack(self, username: str, monster_id: int) -> object:
        pass
