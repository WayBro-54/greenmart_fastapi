from datetime import date
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, relationship, mapped_column
from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from db import Base


class Users(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = 'users'
    agent: Mapped['Agent'] = relationship(back_populates='user')


class Agent(Base):
    __tablename__ = 'agents'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    firstname: Mapped[str] = mapped_column(String(50), nullable=True)
    lastname: Mapped[str] = mapped_column(String(50), nullable=True)
    surname: Mapped[str] = mapped_column(String(50), nullable=True)
    birthday: Mapped[date] = mapped_column(nullable=True)
    phone: Mapped[str] = mapped_column(String(15), unique=True)
    address: Mapped[str] = mapped_column(String(250), nullable=True)
    user: Mapped['Users'] = relationship(back_populates='agent')
