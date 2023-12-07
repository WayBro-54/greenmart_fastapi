from __future__ import annotations
from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from core.db import Base


class User(SQLAlchemyUserDatabase, Base):
    agent: Mapped[Agent] = relationship(back_populates='user')


class Agent(Base):
    id: Mapped[int]
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    user: Mapped[User] = relationship(back_populates='id')
