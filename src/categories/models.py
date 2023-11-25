from sqlalchemy import String, ForeignKey, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship
from core.db import Base


CategoriesProduct = Table(
    'CategoriesProduct',
    Base.metadata,
    Column(
        'product',
        ForeignKey('product.id'),
        primary_key=True,
    ),
    Column(
        'categories',
        ForeignKey('categories.id'),
        primary_key=True,
    ),
)


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
    products: Mapped[list['Product']] = relationship(
        secondary=CategoriesProduct,
        back_populates='categories'
    )
