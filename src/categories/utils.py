from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from categories.crud import category_crud


async def is_exist_code_or_name(
        code: str,
        title: str,
        session: AsyncSession,
):
    is_code = await category_crud.get_categories_id_by_code(code, session)
    is_title = await category_crud.get_categories_id_by_title(title, session)
    if is_code is not None:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail=f'Категория с кодом: [{code}], уже присутствует!'
        )
    if is_title is not None:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail=f'Категория с именем: [{title}], уже присутствует!'
        )


async def is_exist_code_or_name_update(
        id_categories: int,
        code: str,
        title: str,
        session: AsyncSession,
):
    is_code = await category_crud.get_categories_id_by_code_update(
        id_categories,
        code,
        session,
    )
    is_title = await category_crud.get_categories_id_by_title_update(
        id_categories,
        title,
        session,
    )
    if is_code is not None:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail=f'Категория с кодом: [{code}], уже присутствует!'
        )
    if is_title is not None:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail=f'Категория с именем: [{title}], уже присутствует!'
        )


async def get_object_or_404(
        id_categories: int,
        session: AsyncSession
):
    is_exist_db = await category_crud.get(
        id_categories,
        session,
    )
    if is_exist_db is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail=f'Записи с ID={id_categories}, не обнаружено!'
        )
    return is_exist_db
