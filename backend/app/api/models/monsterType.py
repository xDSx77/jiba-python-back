from sqlalchemy import Column, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class MonsterType(Base):
    __tablename__ = 'monster_type'

    id = Column(Integer, primary_key=True, server_default=text("nextval('scraping_id_seq'::regclass)"))
    name = Column(String(50), nullable=False)
    hp_max = Column(Integer, nullable=False)
    damage = Column(Integer, nullable=False)
    xp_value = Column(Integer, nullable=False)
    gold_value = Column(Integer, nullable=False)

    def __init__(self, name, hp_max=1, damage=1, xp_value=1, gold_value=1):
        self.name = name
        self.hp_max = hp_max
        self.damage = damage
        self.xp_value = xp_value
        self.gold_value = gold_value
