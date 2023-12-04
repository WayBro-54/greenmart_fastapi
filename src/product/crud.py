from __future__ import annotations
from typing import TYPE_CHECKING
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert
from sqlalchemy.orm import selectinload

from product.models import Product
from core.crud import CRUDBase

if TYPE_CHECKING:
    from categories.models import CategoriesProduct


class ProductCrud(CRUDBase):

    async def create_list_category(
            self,
            obj_in,
            session: AsyncSession
    ):
        obj_in_data = obj_in.dict()
        categories = obj_in_data.pop('categories')
        db_obj = self.model(**obj_in_data)

        # Создаем новый объект модели Product
        session.add(db_obj)
        await session.flush()
        await session.refresh(db_obj)

        # Используем bulk insert для создания связи  many to namy
        # для модели CategoriesProduct

        db_obj_id = db_obj.id
        data = [{'product_id': db_obj_id,
                 'category_id': cat['id']} for cat in categories]
        await session.execute(insert(CategoriesProduct), data)
        await session.commit()

        # получаем объект повторно, подгрузив категории
        obj = await session.execute(
            select(Product).where(Product.id == db_obj_id).options(
                selectinload(Product.categories)
            )
        )
        return obj.scalar()


product_crud = ProductCrud(Product)
