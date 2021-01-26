from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.core.config import DATABASE_URL

Base = declarative_base()


def connection_uri():
    return DATABASE_URL


URI = connection_uri()
Engine = create_engine(URI, pool_size=50, max_overflow=-1)
Global_session = scoped_session(sessionmaker(bind=Engine))


@contextmanager
def session_scope():
    try:
        yield Global_session()
        Global_session.commit()
    except InvalidRequestError:
        Global_session.rollback()
        raise
