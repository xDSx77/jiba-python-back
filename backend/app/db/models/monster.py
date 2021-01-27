from sqlalchemy import ForeignKey, Column, Integer, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Monster(Base):
    __tablename__ = 'monster'

    id = Column(Integer, primary_key=True, server_default=text("nextval('monster_id_seq'::regclass)"))
    monster_type_id = Column(ForeignKey('monster_type.id'))
    hp = Column(Integer, nullable=False)

    def __init__(self, monster_type_id, hp=1):
        self.monster_type_id = monster_type_id
        self.hp = hp
