from sqlalchemy import ForeignKey, Column, Integer, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class PlayerQuest(Base):
    __tablename__ = 'player_quest'

    id = Column(Integer, primary_key=True, server_default=text("nextval('scraping_id_seq'::regclass)"))
    player_id = Column(ForeignKey('player.id'))
    quest_id = Column(ForeignKey('quest.id'))
    progress = Column(Integer, nullable=False)

    def __init__(self, player_id, quest_id, progress=0):
        self.player_id = player_id
        self.quest_id = quest_id
        self.progress = progress
