import random
import time

import requests
from sqlalchemy import insert, select
from sqlalchemy.orm import sessionmaker

from main import engine
from models import Group, AllBase

Session = sessionmaker(bind=engine)


# Получение всех id групп, которые хранятся в БД
# allGroups = []

# with Session() as session:
#     try:
#         for i in session.scalars(select(Group)).fetchall():
#             allGroups.append(i.id)
#     except:
#         session.rollback()
#         raise
#     else:
#         session.commit()
#
# for i in allGroups:
#     with Session() as session:
#         try:
#             session.scalars(select(AllBase.group).where(AllBase.group == i) .group_by(AllBase.group)).one()
#         except:
#             print(i)
#         else:
#             session.commit()


# Запись информации каждой группы в БД
# for groupa in allGroups:
#     response = requests.post('https://miet.ru/schedule/data', {'group': groupa}).json()['Data']
#     for i in response:
#         groupId = 0
#         with Session() as session:
#             try:
#                 st = select(Group).where(Group.name == i['Group']['Name'])
#                 groupId = session.scalars(st).one().id
#             except:
#                 session.rollback()
#                 raise
#             else:
#                 session.commit()
#
#         with Session() as session:
#             try:
#                 session.add(AllBase(
#                     name=i['Class']['Name'],
#                     room=i['Room']['Name'],
#                     group=groupId,
#                     day=i['Day'],
#                     dayNumber=i['DayNumber'],
#                     time=i['Time']['Code'],
#                 ))
#                 print(groupa, ' была добавлена в базу')
#             except:
#                 session.rollback()
#                 print('Случилась ошибка при добавлении')
#                 raise
#             else:
#                 session.commit()
#     time.sleep(1)


# Получение запись всех групп в БД
# response = requests.post('https://miet.ru/schedule/groups').json()
# Session = sessionmaker(bind=engine)

# for i in response:
#     with Session() as session:
#         try:
#             session.add(Group(name=i))
#         except:
#             session.rollback()
#             raise
#         else:
#             session.commit()


