from typing import Optional
from sqlalchemy import types
from sqlalchemy import String, ForeignKey, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship
from core.db import Base

# Промежуточная таблица между Product и Categories
CategoriesProduct = Table(
    'CategoriesProduct',
    Base.metadata,
    Column(
        'product_id',
        ForeignKey('product.id'),
        primary_key=True,
        # nullable=True,
        # null=True,
    ),
    Column(
        'categories_id',
        ForeignKey('categories.id'),
        primary_key=True,
        # nullable=True,
        # null=True,
    ),
)


class Categories(Base):
    ''' Таблица с категориями '''
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
    description: Mapped[Optional[str]] = mapped_column(nullable=True)
    products: Mapped[
        Optional[list['Product']]
    ] = relationship(
        secondary=CategoriesProduct,
        back_populates='categories',
    )
