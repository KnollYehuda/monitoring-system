from datetime import datetime
from typing import Any

from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import declarative_base

Base: Any = declarative_base()


class Image(Base):
    __tablename__ = "images"

    id = Column("id", Integer(), primary_key=True)
    name = Column("name", String(255), nullable=False)
    source = Column("source", String(255), nullable=False)
    date_created = Column("date_created", DateTime, default=datetime.utcnow())

    def __init__(self, name, source):
        self.name = name
        self.source = source

    def __repr__(self):
        return "<Image(id='%s', name='%s', source='%s', date_created='%s')>" % (
            self.id,
            self.name,
            self.source,
            self.date_created,
        )
