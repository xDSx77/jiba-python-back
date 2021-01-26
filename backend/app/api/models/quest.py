from sqlalchemy import ForeignKey, Column, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Quest(Base):
    __tablename__ = 'quest'

    id = Column(Integer, primary_key=True, server_default=text("nextval('scraping_id_seq'::regclass)"))
    name = Column(String(50), nullable=False)
    monster_type_id = Column(ForeignKey('monster_type.id'))
    goal = Column(Integer, nullable=False)
    xp_value = Column(Integer, nullable=False)
    gold_value = Column(Integer, nullable=False)

    def __init__(self, name, monster_type_id, goal=1, xp_value=1, gold_value=1):
        self.name = name
        self.monster_type_id = monster_type_id
        self.goal = goal
        self.xp_value = xp_value
        self.gold_value = gold_value
