from typing import Optional
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from base import Categories, CategoriesProduct
from core.db import Base
from base_model import NonNegativeInteger


class Product(Base):
    '''Таблица с продутов.'''
    id: Mapped[int] = mapped_column(
        unique=True,
        primary_key=True,
    )
    title: Mapped[str] = mapped_column(
        String(250),
    )
    code: Mapped[int] = mapped_column(unique=True)
    categories: Mapped[Optional[list['Categories']]] = relationship(
        secondary=CategoriesProduct.__table__,
        back_populates='products',
    )
    description: Mapped[Optional[str]]
    country: Mapped[Optional[str]] = mapped_column(String(255))
    count: Mapped[Optional[int]]
