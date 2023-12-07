from __future__ import annotations
from typing import Optional, TYPE_CHECKING
from sqlalchemy import String
from sqlalchemy.orm import (Mapped, mapped_column, relationship,
                            validates)
from core.db import Base

if TYPE_CHECKING:
    from base import (Categories, Orders, OrdersProduct)
    from categories.models import CategoriesProduct

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
    description: Mapped[Optional[str]]
    country: Mapped[Optional[str]] = mapped_column(String(255))
    count: Mapped[Optional[int]]
    is_deleted: Mapped[int] = mapped_column(
        default=0,
    )
    categories: Mapped[Optional[list['Categories']]] = relationship(
        secondary='CategoriesProduct.__table__',
        back_populates='products',
    )
    orders: Mapped[Optional[list[Orders]]] = relationship(
        secondary='OrdersProduct.__table__',
        back_populates='products',
    )

    @validates('is_deleted')
    def validate_is_deleted(self, key, value):
        if value not in [0, 1]:
            raise ValueError(f'is_deleted принимает 0 или 1. value: [{value}]')
        return value
