from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends
from orders.shemas import CreateOrder, DBOrder
from core.db import get_async_session
from orders.crud import order_crud


order_router = APIRouter()

@order_router.post(
    '/',
    response_model_exclude_none=True,
    description='Create new order'
)
async def create_order(
        obj_in: CreateOrder,
        session: AsyncSession = Depends(get_async_session),
):
    res = await order_crud.create(obj_in, session)
    return res
