import sqlalchemy
import sqlite3

engine = sqlalchemy.create_engine('sqlite:///../db/database.db')
conn = engine.connect()
metadata = sqlalchemy.MetaData()
inspetor = sqlalchemy.inspect(engine)




