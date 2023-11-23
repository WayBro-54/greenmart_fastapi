from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
#
from categories.shemas import (CategoryDB, CategoryCreate,
                               CategoryUpdate)
from categories.crud import category_crud
from core.db import get_async_session
from categories.utils import is_exist_code_or_name, is_exist_id

category_router = APIRouter()


@category_router.get(
    '/{category_id}',
    response_model=CategoryDB,
    response_model_exclude_none=True,
)
async def get_category(
    category_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    '''
    Эндпоинт для просмотра категории
    '''
    category = await category_crud.get(category_id, session)
    return category


@category_router.get(
    '/',
    response_model=list[CategoryDB],
    response_model_exclude_none=True,
)
async def get_all_category(
        session: AsyncSession = Depends(get_async_session)
):
    '''
    Эндпоинт для просмотра всех категорий
    '''
    all_category = await category_crud.get_all(session)
    return all_category

@category_router.post(
    '/',
    response_model=CategoryDB,
    response_model_exclude_none=True,
)
async def create_category(
        category_data: CategoryCreate,
        session: AsyncSession = Depends(get_async_session)
):
    '''
    Эндпоинт для создания категории
    '''
    await is_exist_code_or_name(
        category_data.code,
        category_data.title,
        session,
    )
    category = await category_crud.create(category_data, session)
    return category


@category_router.patch(
    '/',
    response_model=CategoryDB,
    response_model_exclude_none=True,
)
async def update_category(
        category_id: int,
        categories_in: CategoryUpdate,
        session: AsyncSession = Depends(get_async_session),
):
    '''
    Эндпоинт для обновления категории
    '''
    await is_exist_id(category_id, session)
