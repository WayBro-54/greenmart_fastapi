from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from categories.models import Categories
from categories.crud import category_crud
from core.validators import BaseValidation


class CategoryValidator(BaseValidation):

    async def is_exist_code_or_name(
            self,
            code: str,
            title: str,
            session: AsyncSession,
    ):
        is_code = await self.crud.get_categories_id_by_code(code, session)
        is_title = await self.crud.get_categories_id_by_title(title, session)
        if is_code is not None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f'Категория с кодом: [{code}], уже присутствует!'
            )
        if is_title is not None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f'Категория с именем: [{title}], уже присутствует!'
            )

    async def is_exist_code_or_name_update(
            self,
            id_categories: int,
            code: str,
            title: str,
            session: AsyncSession,
    ):
        is_code = await self.crud.get_categories_id_by_code_update(
            id_categories,
            code,
            session,
        )
        is_title = await self.crud.get_categories_id_by_title_update(
            id_categories,
            title,
            session,
        )
        if is_code is not None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f'Категория с кодом: [{code}], уже присутствует!'
            )
        if is_title is not None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f'Категория с именем: [{title}], уже присутствует!'
            )



category_validator = CategoryValidator(Categories, category_crud)
