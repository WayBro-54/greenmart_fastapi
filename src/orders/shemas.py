from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, field_validator


class ListInfoProduct(BaseModel):
    product: int
    count_product: int
    price_product: int

    @field_validator('product', 'count_product', 'price_product') # noqa
    @classmethod
    def validate_info_producut(cls, value: int):
        if isinstance(value, int):
            if value < 0:
                raise ValueError(f'product, count_product, cannot be negative value!{value}')
        return value


class BaseOrder(BaseModel):
    pass


class Order(BaseOrder):
    pass


class ListOrder(BaseOrder):
    pass


class CreateOrder(BaseOrder):
    products: list[ListInfoProduct]
    # date_order: Optional[datetime] = Field(default=)



class UpdateOrder(BaseOrder):
    pass


class DBOrder(BaseOrder):
    id: int
    product_id: list[int]
    total_price: int
    count_product: int
    payments: bool
    date_order: datetime




