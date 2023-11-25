from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.encoders import jsonable_encoder

from core.crud import CRUDBase
from categories.models import Categories


class CategoriesCRUD(CRUDBase):
    async def get_categories_id_by_code(
            self,
            code: str,
            session: AsyncSession,
    ):
        db_categories_id = await session.execute(
            select(
                self.model.id
            ).where(self.model.code == code)
        )
        db_categories_id = db_categories_id.scalars().first()
        return db_categories_id

    async def get_categories_id_by_title(
            self,
            title: str,
            session: AsyncSession,
    ):
        db_categories_id = await session.execute(
            select(
                self.model.id
            ).where(self.model.title == title)
        )
        db_categories_id = db_categories_id.scalars().first()
        return db_categories_id

    async def get_categories_id_by_code_update(
            self,
            id_category: int,
            code: str,
            session: AsyncSession,
    ):
        db_categories_id = await session.execute(
            select(
                self.model.id
            ).where(
                and_(
                    self.model.code == code,
                    self.model.id != id_category
                )
        )
        )
        db_categories_id = db_categories_id.scalars().first()
        return db_categories_id

    async def get_categories_id_by_title_update(
            self,
            id_category: int,
            title: str,
            session: AsyncSession,
    ):
        db_categories_id = await session.execute(
            select(
                self.model.id
            ).where(
                and_(
                    self.model.title == title,
                    self.model.id != id_category
                )
            )
        )
        db_categories_id = db_categories_id.scalars().first()
        return db_categories_id


category_crud = CategoriesCRUD(Categories)
