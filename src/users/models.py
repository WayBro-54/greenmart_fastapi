
# from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.orm import Mapped, mapped_column
from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from db import Base


class Users(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = 'users'
    # id: Mapped[int] = mapped_column(primary_key=True)
    pass
    # agent: Mapped[Agent] = relationship(back_populates='user')


# class Agent(Base):
#     id: Mapped[int]
#     user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
#     user: Mapped[User] = relationship(back_populates='id')
