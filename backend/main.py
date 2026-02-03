import sqlite3

from sqlalchemy import create_engine, MetaData, inspect, select, func
from sqlalchemy.orm import sessionmaker
from models import Base, Group, AllBase

engine = create_engine('sqlite:///../db/database.db')
inspetor = inspect(engine)
Session = sessionmaker(bind=engine)

with Session() as session:
    try:
        for i in session.scalars(select(AllBase.group, func.count(AllBase.name).label('count')).group_by(AllBase.group)).all():
            print(i.group, i.count)
    except:
        session.rollback()
        raise
    else:
        session.commit()

