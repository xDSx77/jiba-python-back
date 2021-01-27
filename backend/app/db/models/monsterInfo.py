from sqlalchemy import Column, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from app.db.session import Engine

Base = declarative_base()


class MonsterInfo(Base):
    __table__ = Table('monster_info', Base.metadata, Column('id', Integer, primary_key=True), autoload=True, autoload_with=Engine)

    def __init__(self, id, monster_type_id, name, hp_max, damage, xp_value, gold_value, hp):
        self.id = id
        self. monster_type_id = monster_type_id
        self.name = name
        self.hp_max = hp_max
        self.damage = damage
        self.xp_value = xp_value
        self.gold_value = gold_value
        self.hp = hp