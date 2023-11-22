from fastapi import APIRouter
from categories.router import category_router

main_router = APIRouter()

main_router.include_router(
    category_router,
    prefix='/category',
    tags=['Category']
)
