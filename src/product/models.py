from typing import Optional
from sqlalchemy import String
from sqlalchemy.orm import (Mapped, mapped_column, relationship,
                            validates)

from base import Categories, CategoriesProduct
from core.db import Base


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
    is_deleted: Mapped[int] = mapped_column(
        default=0,
    )

    @validates('is_deleted')
    def validate_is_deleted(self, key, value):
        if value not in [0, 1]:
            raise ValueError(f'is_deleted принимает 0 или 1. value: [{value}]')
        return value
