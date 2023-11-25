from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from core.db import Base


class Categories(Base):
    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )
    code: Mapped[str] = mapped_column(
        String(30),
        unique=True,
    )
    title: Mapped[str] = mapped_column(
        String(250),
        unique=True,
    )
    description: Mapped[str]
