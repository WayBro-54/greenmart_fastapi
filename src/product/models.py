from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from base import Categories, CategoriesProduct
from core.db import Base
from base_model import NonNegativeInteger


class Product(Base):
    id: Mapped[int] = mapped_column(
        unique=True,
        primary_key=True,
    )
    title: Mapped[str] = mapped_column(
        String(250),
    )
    code: Mapped[NonNegativeInteger]
    categories: Mapped[list['Categories']] = relationship(
        secondary=CategoriesProduct,
        back_populates='products',
    )
    description: Mapped[str]
    country: Mapped[str] = mapped_column(String(255))
    count: Mapped[int]
