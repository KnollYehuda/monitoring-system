from datetime import datetime
from typing import Any

from sqlalchemy import Column, DateTime, Enum, Integer, String
from sqlalchemy.orm import declarative_base

Base: Any = declarative_base()


class Task(Base):
    __tablename__ = "tasks"

    id = Column("id", Integer(), primary_key=True)
    name = Column("name", String(255), nullable=False)
    content = Column("content", String(255), nullable=False)
    status = Column("status", Enum("pending", "failed", "success"), default="pending")  # type: Column
    date_created = Column("date_created", DateTime, default=datetime.utcnow())

    def __repr__(self):
        return "<Task(id='%s', name='%s', content='%s', status='%s', date_created='%s')>" % (
            self.id,
            self.name,
            self.content,
            self.status,
            self.date_created,
        )
