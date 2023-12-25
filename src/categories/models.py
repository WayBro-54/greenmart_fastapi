from typing import Optional
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from core.db import Base



# Промежуточная таблица между Product и Categories
class CategoriesProduct(Base):
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'), primary_key=True)
    product_id: Mapped[int] = mapped_column(ForeignKey('product.id'), primary_key=True)


class Categories(Base):
    ''' Таблица с категориями '''
    id: Mapped[int] = mapped_column(
        primary_key=True,
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
        secondary=CategoriesProduct.__table__,
        back_populates='categories',
    )
