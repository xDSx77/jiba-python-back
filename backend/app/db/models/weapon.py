from sqlalchemy import Column, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Weapon(Base):
    __tablename__ = 'weapon'

    id = Column(Integer, primary_key=True, server_default=text("nextval('scraping_id_seq'::regclass)"))
    name = Column(String(50), nullable=False)
    damage = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)

    def __init__(self, name, damage=1, price=1):
        self.name = name
        self.protection = damage
        self.price = price
