from sqlalchemy import (
    Boolean,
    Column,
    Enum,
    Integer,
    MetaData,
    String,
    Table,
    create_engine,
)

engine = create_engine("db+postgresql://guest:guest@postgres:5432/")
conn = engine.connect()
metadata = MetaData()

Student = Table(
    "tasks",
    metadata,
    Column("id", Integer(), primary_key=True),
    Column("name", String(255), nullable=False),
    Column("status", Enum("pending", "failed", "success")),
)

metadata.create_all(engine)
