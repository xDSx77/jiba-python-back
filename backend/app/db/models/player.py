from sqlalchemy import ForeignKey, Column, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Player(Base):
    __tablename__ = 'player'

    id = Column(Integer, primary_key=True, server_default=text("nextval('scraping_id_seq'::regclass)"))
    username = Column(String(50), nullable=False)
    level = Column(Integer, nullable=False)
    xp = Column(Integer, nullable=False)
    xp_max = Column(Integer, nullable=False)
    hp = Column(Integer, nullable=False)
    hp_max = Column(Integer, nullable=False)
    gold = Column(Integer, nullable=False)
    weapon_id = Column(ForeignKey('weapon.id'))
    armor_id = Column(ForeignKey('armor.id'))

    def __init__(self, username, level=1, xp=0, xp_max=100, hp=10, hp_max=10, gold=0):
        self.username = username
        self.level = level
        self.xp = xp
        self.xp_max = xp_max
        self.hp = hp
        self.hp_max = hp_max
        self.gold = gold
