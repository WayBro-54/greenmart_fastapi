from __future__ import annotations
from typing import TYPE_CHECKING
from fastapi.encoders import jsonable_encoder
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert, delete
from sqlalchemy.orm import selectinload, noload

from product.models import Product
from core.crud import CRUDBase

if TYPE_CHECKING:
    from categories.models import CategoriesProduct, Categories


class ProductCrud(CRUDBase):

    async def get_product(
            self,
            id_product: int,
            session: AsyncSession,
    ):
        product = await session.execute(
            select(Product).where(
                Product.id == id_product
            ).options(
                selectinload(Product.categories)
            )
        )
        return product.scalar_one_or_none()

    async def get_all_products(
            self,
            session: AsyncSession
    ):
        all_products = await session.execute(
            select(Product).where(
                Product.is_deleted == 0
            ).options(
                selectinload(Product.categories)
            )
        )
        return all_products.scalars()

    async def create_list_category(
            self,
            obj_in,
            session: AsyncSession
    ):
        obj_in_data = obj_in.dict()
        categories = obj_in_data.pop('categories')
        print(obj_in_data)
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

    async def update_product(
            self,
            obj_in,
            obj_db,
            session: AsyncSession,
    ):
        obj_in_data = jsonable_encoder(obj_in)
        obj_db_data = jsonable_encoder(obj_db)

        category_in_data = obj_in_data.pop('categories')
        # category_db_data = obj_db_data.pop('categories')
        db_obj_id = obj_db_data.id
        for field in obj_db_data:
            if field in obj_in_data:
                setattr(obj_db_data, field, obj_in_data[field])

        session.add(obj_db_data)
        await session.commit()
        await session.refresh(obj_db_data)

        await session.execute(
            delete(CategoriesProduct).where(CategoriesProduct.product_id == obj_db_data['id'])
        )

        data = [{'product_id': db_obj_id,
                 'category_id': cat['id']} for cat in category_in_data]

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
