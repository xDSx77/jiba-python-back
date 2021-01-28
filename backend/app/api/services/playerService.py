from typing import Dict, List, Union

from app.db.models.player import Player
from app.db.repositories import PlayerRepository
from app.db.repositories import MonsterInfoRepository
from app.db.repositories import MonsterRepository


class PlayerService:

    def __init__(self):
        self.player_repository = PlayerRepository()
        self.monster_info_repository = MonsterInfoRepository()
        self.monster_repository = MonsterRepository()

    def get_all_players(self) -> List[Player]:
        return self.player_repository.get_all()

    def create_new_player(self, username: str):
        new_player = None
        if self.player_repository.get_by_username(username) is None:
            new_player = Player(username=username)
            self.player_repository.save(new_player)
        return new_player

    def get_player_info(self, username: str):
        return self.player_repository.get_by_username(username)

    def rest(self, username: str):
        player = self.player_repository.get_by_username(username)
        updated_player = Player(player.username,
                                player.level,
                                player.xp,
                                player.xp_max,
                                min(player.hp + 5, player.hp_max),
                                player.hp_max,
                                player.gold)
        self.player_repository.update_by_username(updated_player)
        return self.player_repository.get_by_username(username)

    def attack(self, username: str, monster_id: int) -> Dict[str, Union[str, bool]]:
        player = self.player_repository.get_by_username(username)
        if player is None:
            return {"error": "Unknown player"}
        monster_info = self.monster_info_repository.get_by_id(monster_id)
        monster = self.monster_repository.get_by_monster_id(monster_id)
        if monster is None:
            return {"error": "Unknown monster"}
        monster.hp -= player.level

        died = False
        level_up = False

        if monster.hp <= 0:
            player.xp += monster_info.xp_value
            player.gold += monster_info.gold_value
        else:
            player.hp = max(player.hp - monster_info.damage, 0)

        while player.xp >= player.xp_max:
            player.level += 1
            player.xp -= player.xp_max
            player.xp_max *= 1.8
            player.hp_max += 5
            player.hp = player.hp_max
            level_up = True

        if player.hp <= 0:
            died = True
            player.hp = player.hp_max
            player.gold = int(player.gold/2)

        damage_taken = monster_info.damage
        xp_reward = monster_info.xp_value
        gold_reward = monster_info.gold_value

        if monster.hp <= 0:
            self.monster_repository.delete_by_id(monster.id)
        else:
            self.monster_repository.update_by_id(monster)

        self.player_repository.update_by_username(player)

        return {
            "player": player,
            "damage_taken": damage_taken,
            "gold_reward": gold_reward,
            "xp_reward": xp_reward,
            "monster_died": monster.hp <= 0,
            "player_died": died,
            "level_up": level_up
        }
