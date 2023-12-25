from sqlalchemy.ext.asyncio import AsyncSession
from core.crud import CRUDBase
from orders.models import Orders
from fastapi.encoders import jsonable_encoder


class OrderCRUD(CRUDBase):
    async def create(
            self,
            obj_in,
            session: AsyncSession
    ):
        obj_in_date = jsonable_encoder(obj_in)
        print(obj_in_date)
        products = obj_in_date.pop('products')
        for product in products:
            obj = self.model(product)
            session.add(obj)
            await session.flush()
            await session.refresh(obj)





order_crud = OrderCRUD(Orders)
