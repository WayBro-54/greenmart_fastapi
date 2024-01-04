from typing import Optional, TYPE_CHECKING
from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


from db import Base

if TYPE_CHECKING:
    from base import Product


class OrdersProduct(Base):
    __tablename__ = 'orders_products'
    product_id: Mapped[int] = mapped_column(ForeignKey('product.id'), primary_key=True)
    order_id: Mapped[int] = mapped_column(ForeignKey('orders.id'), primary_key=True)


class Orders(Base):
    __tablename__ = 'orders'
    id: Mapped[int] = mapped_column(primary_key=True)
    count_product: Mapped[int]
    price_product: Mapped[int]
    # product_id: Mapped['Product'] = relationship(back_populates='orders')
    products: Mapped[list['Product']] = relationship(
        secondary=OrdersProduct.__table__,
        back_populates='orders',
    )
    order_detail_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey('order_detail.id')
    )
    order_detail: Mapped['OrderDetail'] = relationship(back_populates='orders')


class OrderDetail(Base):
    __tablename__ = 'order_detail'
    id: Mapped[int] = mapped_column(primary_key=True)
    date_order: Mapped[datetime] = mapped_column(
        default=datetime.now,
    )
    is_paid: Mapped[bool] = mapped_column(default=False)
    date_paid: Mapped[Optional[datetime]]
    orders: Mapped[list['Orders']] = relationship(back_populates='order_detail')
    # user: Mapped[int] = mapped_column(ForeignKey('users.id'))