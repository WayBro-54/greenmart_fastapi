from fastapi import APIRouter
from categories.router import category_router
from product.router import product_router
from orders.router import order_router
from users.endpoint.users import user_router
from users.endpoint.agent import agent_router

main_router = APIRouter()

main_router.include_router(
    category_router,
    prefix='/category',
    tags=['Category'],
)

main_router.include_router(
    product_router,
    prefix='/product',
    tags=['Product'],
)

main_router.include_router(
    order_router,
    prefix='/order',
    tags=['Order'],
)

main_router.include_router(
    user_router
)

main_router.include_router(
    agent_router,
    prefix='/agent',
    tags=['Agent'],
)
