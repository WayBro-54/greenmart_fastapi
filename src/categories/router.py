from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from categories.shemas import (CategoryDB, CategoryCreate,
                               CategoryUpdate)
from categories.crud import category_crud
from categories.validators import category_validator
from db import get_async_session
from users.models import Users
from users.config import current_superuser

category_router = APIRouter()


@category_router.get(
    '/{category_id}',
    response_model=CategoryDB,
    response_model_exclude_none=True,
    description='get category'
)
async def get_category(
    category_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    category = await category_crud.get(category_id, session)
    return category


@category_router.get(
    '/',
    response_model=list[CategoryDB],
    response_model_exclude_none=True,
    description='Get data list category',
)
async def get_all_category(
        session: AsyncSession = Depends(get_async_session)
):
    all_category = await category_crud.get_all(session)
    return all_category


@category_router.post(
    '/',
    response_model=CategoryDB,
    response_model_exclude_none=True,
    description='create a new category',
)
async def create_category(
        category_data: CategoryCreate,
        session: AsyncSession = Depends(get_async_session),
        user: Users = Depends(current_superuser),
):
    await category_validator.is_superuser(user)
    await category_validator.is_exist_code_or_name(
        category_data.code,
        category_data.title,
        session,
    )
    category = await category_crud.create(category_data, session)
    return category


@category_router.patch(
    '/{category_id}/update',
    response_model=CategoryDB,
    response_model_exclude_none=True,
    description='Update category',
)
async def update_category(
        category_id: int,
        categories_in: CategoryUpdate,
        session: AsyncSession = Depends(get_async_session),
        user: Users = Depends(current_superuser),
):
    await category_validator.is_superuser(user)
    db_category = await category_validator.get_object_or_404(category_id, session,)
    await category_validator.is_exist_code_or_name_update(
        category_id,
        categories_in.code,
        categories_in.title,
        session,
    )
    upd_categories = await category_crud.update(
        db_category,
        categories_in,
        session,
    )
    return upd_categories


@category_router.delete(
    '{id_category}/delete',
    response_model=CategoryDB,
    response_model_exclude_none=True,
    description='Delete category',
)
async def delete_category(
    category_id,
    session: AsyncSession = Depends(get_async_session),
    user: Users = Depends(current_superuser),
):
    await category_validator.is_superuser(user)
    obj = await category_validator.get_object_or_404(category_id, session)
    rm_obj = await category_crud.remove(obj, session)
    return rm_obj
