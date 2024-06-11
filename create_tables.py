from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from start_session import engine


Base = declarative_base()


class Defects(Base):
    __tablename__ = "defects"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    defect = Column("defect", String(255))
    name_of_works = Column("name_of_works", String(255))
    unit = Column("unit", String(255))
    number = Column("number", Integer)


class Workers(Base):
    __tablename__ = "workers"
   
    id = Column("id", Integer, primary_key=True)
    worker = Column("worker", Integer)
    lastname = Column("lastname", String(255))
    firstname = Column("firstname", String(255))
    surname = Column("surname", String(255))
    sheet_amount = Column("sheet_amount", Integer)


Base.metadata.create_all(engine)