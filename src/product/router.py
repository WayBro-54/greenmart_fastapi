from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db import get_async_session
from .validators import product_validator
from product.shemas import ProductDB, ProductCreate, ProductUpdate
from product.crud import product_crud
from users.models import Users
from users.config import current_superuser


product_router = APIRouter()


@product_router.get(
    '/{id_product}',
    response_model=ProductDB,
    response_model_exclude_none=True,
    description='product information'
)
async def get_product(
        id_product: int,
        session: AsyncSession = Depends(get_async_session)
):
    db_obj = await product_validator.get_object_or_404(id_product, session)
    return db_obj


@product_router.get(
    '/',
    response_model=list[ProductDB],
    response_model_exclude_none=True,
    description='View all products',
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
    description='add product',
)
async def product_create(
        obj_in: ProductCreate,
        user: Users = Depends(current_superuser),
        session: AsyncSession = Depends(get_async_session)
):
    await product_validator.is_superuser(user)

    product = await product_crud.create_list_category(obj_in, session)
    return product


@product_router.patch(
    '/{product_id}/update',
    response_model=ProductDB,
    response_model_exclude_none=True,
    description='update product',
)
async def product_update(
    product_id: int,
    obj_in: ProductUpdate,
    user: Users = Depends(current_superuser),
    session: AsyncSession = Depends(get_async_session),
):
    await product_validator.is_superuser(user)

    obj_db = await product_validator.get_object_or_404(product_id, session)
    res = await product_crud.update_product(
        obj_in,
        obj_db,
        session
    )
    return res


@product_router.delete(
    '/{product_id}',
    response_model=ProductDB,
    response_model_exclude_none=True,
    description='delete product',
)
async def product_remove(
    product_id: int,
    user: Users = Depends(current_superuser),
    session: AsyncSession = Depends(get_async_session)
):
    await product_validator.is_superuser(user)

    obj_db = await product_validator.get_object_or_404(product_id, session)

    await session.delete(obj_db)
    await session.commit()
