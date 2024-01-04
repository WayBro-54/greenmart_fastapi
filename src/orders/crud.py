from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from core.crud import CRUDBase
from orders.models import Orders, OrdersProduct, OrderDetail
from fastapi.encoders import jsonable_encoder


class OrderCRUD(CRUDBase):
    async def create(
            self,
            obj_in,
            session: AsyncSession
    ):
        obj_in_date = jsonable_encoder(obj_in)

        # create object order_detail for added objects products
        order_detail = OrderDetail(
            date_order=datetime.now(),
            is_paid=False,
        )
        session.add(order_detail)
        await session.flush()

        # create orders list and connect to order_detail
        for product in obj_in_date['products']:
            product_id = product.pop('product')
            product['order_detail_id'] = order_detail.id
            obj = self.model(**product)

            session.add(obj)
            await session.flush()
            await session.refresh(obj)

            # connect object order and product, connect - Many to Many
            order_product = OrdersProduct(product_id=product_id, order_id=obj.id)

            session.add(order_product)
            await session.commit()





order_crud = OrderCRUD(Orders)
