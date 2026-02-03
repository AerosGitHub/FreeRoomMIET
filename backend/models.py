from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, foreign


class Base(DeclarativeBase):
    pass

class Group(Base):
    __tablename__ = "groups"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(300))

class AllBase(Base):
    __tablename__ = "all_base"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(300))
    room: Mapped[str] = mapped_column(String(300))
    group: Mapped[int] = mapped_column(ForeignKey(Group.id))
    day: Mapped[int] = mapped_column(Integer)
    dayNumber: Mapped[int] = mapped_column(Integer)
    time: Mapped[int] = mapped_column(Integer)

