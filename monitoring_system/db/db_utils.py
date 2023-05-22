from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ..consts import DB_CONNECTION_STRING

db = create_engine(DB_CONNECTION_STRING)
conn = db.connect()


def session_maker():
    """Create a database connection session"""
    session = sessionmaker(db)
    return session()
