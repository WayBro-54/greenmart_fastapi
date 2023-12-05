from typing import Union
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.db import get_async_session
from product.shemas import ProductDB, ProductCreate, ProductUpdate
from product.crud import product_crud


product_router = APIRouter()


@product_router.get(
    '/{id_product}',
    response_model=ProductDB,
    response_model_exclude_none=True,
    description='Информация о продукте'
)
async def get_product(
        id_product: int,
        session: AsyncSession = Depends(get_async_session)
):
    db_obj = await product_crud.get(id_product, session)
    return db_obj


@product_router.get(
    '/',
    response_model=list[ProductDB],
    response_model_exclude_none=True,
    description='Просмотр всех продуктов, не удаленных продуктов',
)
async def get_product_all(
        session: AsyncSession = Depends(get_async_session)
):
    product_list = await product_crud.get_all_products(session)
    return product_list


@product_router.post(
    '/',
    response_model=ProductDB,
    response_model_exclude_none=True,
    description='Добавление продукта',
)
async def product_create(
        obj_in: ProductCreate,
        session: AsyncSession = Depends(get_async_session)
):
    product = await product_crud.create_list_category(obj_in, session)
    print(product)
    return product


@product_router.patch(
    '/{product_id}/update',
    response_model=ProductDB,
    response_model_exclude_none=True,
    description='Изменение продукта',
)
async def product_update(
        obj_in: ProductUpdate,
        session: AsyncSession = Depends(get_async_session)
):
    # obj_db = await product_crud.
    pass

@product_router.delete(
    '/{product_id}',
    response_model=ProductDB,
    response_model_exclude_none=True,
    description='Удаление продукта',
)
async def product_remove(
        session: AsyncSession = Depends(get_async_session)
):
    pass
