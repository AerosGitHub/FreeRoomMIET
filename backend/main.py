import sqlite3

from sqlalchemy import create_engine, MetaData, inspect
from sqlalchemy.orm import sessionmaker

from models import Base

engine = create_engine('sqlite:///../db/database.db')
inspetor = inspect(engine)
Session = sessionmaker(bind=engine)

