from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class MonsterInfo(Base):
    __tablename__ = 'monster_info'

    id = Column(Integer, primary_key=True)
    monster_type_id = Column(Integer, nullable=False)
    name = Column(String(50), nullable=False)
    hp_max = Column(Integer, nullable=False)
    damage = Column(Integer, nullable=False)
    xp_value = Column(Integer, nullable=False)
    gold_value = Column(Integer, nullable=False)
    hp = Column(Integer, nullable=False)

    def __init__(self, id, monster_type_id, name, hp_max, damage, xp_value, gold_value, hp):
        self.id = id,
        self. monster_type_id = monster_type_id
        self.name = name
        self.hp_max = hp_max
        self.damage = damage
        self.xp_value = xp_value
        self.gold_value = gold_value
        self.hp = hp
