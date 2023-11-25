from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from core.db import Base


class Product(Base):
    id: Mapped[int] = mapped_column(
        unique=True,
        primary_key=True,
    )
    name: Mapped[str] = mapped_column(
        String(250),
    )
    description: Mapped[str]
    country: Mapped[str] = mapped_column(String(255))
    count: Mapped[int]
