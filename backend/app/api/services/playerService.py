from app.db.models.monster import Monster
from app.db.models.player import Player
from app.db.repositories import PlayerRepository
from app.db.repositories import MonsterInfoRepository
from app.db.repositories import MonsterRepository


class PlayerService:

    def __init__(self):
        self.player_repository = PlayerRepository()
        self.monster_info_repository = MonsterInfoRepository()
        self.monster_repository = MonsterRepository()

    def get_all_players(self):
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
                                max(min(player.hp + 5, player.hp_max), player.hp_max),
                                player.hp_max,
                                player.gold)
        self.player_repository.update_by_username(updated_player)
        return self.player_repository.get_by_username(username)

    def attack(self, username: str, monster_id: int) -> object:
        player = self.player_repository.get_by_username(username)
        monster_info = self.monster_info_repository.get_by_id(monster_id)
        updated_monster = Monster(monster_id,
                                  max(monster_info.hp - player.level, 0))
        updated_player_xp = player.xp
        updated_player_level = player.level
        updated_player_xp_max = player.xp_max
        updated_hp_max = player.hp_max
        updated_hp = player.hp
        updated_gold = player.gold
        died = False
        levelUp = False

        if updated_monster.hp <= 0:
            updated_player_xp += monster_info.xp_value
            updated_gold += monster_info.gold_value
        else:
            updated_hp = max(player.hp - monster_info.damage, 0)

        if updated_player_xp >= player.xp_max:
            updated_player_level += 1
            updated_player_xp -= player.xp_max
            updated_player_xp_max *= 1.8
            updated_hp_max += 5
            updated_hp = updated_hp_max
            levelUp = True

        if updated_hp <= 0:
            died = True
            updated_hp = updated_hp_max
            updated_gold = int(player.gold/2)

        updated_player = Player(player.username,
                                updated_player_level,
                                updated_player_xp,
                                updated_player_xp_max,
                                updated_hp,
                                updated_hp_max,
                                updated_gold)
        if updated_monster.hp <= 0:
            self.monster_repository.delete_by_id(updated_monster.id)
        else:
            self.monster_repository.update_by_id(updated_monster)
            monster_info = self.monster_info_repository.get_by_id(id)

        self.player_repository.update_by_username(updated_player)

        return {
            "player": updated_player,
            "monster_info": monster_info,
            "monster_died": updated_monster.hp <= 0,
            "player_died": died,
            "levelUp": levelUp
        }
