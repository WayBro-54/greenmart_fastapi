from fastapi.encoders import jsonable_encoder
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert
from sqlalchemy.orm import noload

from core.crud import CRUDBase
from product.models import Product
from categories.crud import category_crud

GET_CATEGORY = {
        'id': category_crud.get,
        'title': category_crud.get_categories_id_by_title,
        'code': category_crud.get_categories_id_by_code,
    }


class ProductCrud(CRUDBase):

    async def create_list_category(
        self,
        obj_in,
        session: AsyncSession
    ):
        obj_in_data = obj_in.dict()
        categories = obj_in_data.pop('categories')
        db_obj = self.model(**obj_in_data)
        session.add(db_obj)

        await session.commit()
        await session.refresh(db_obj, ['categories'])

        for category in categories:
            id_category = await category_crud.get_categories_id_code_title(
                category['id'],
                session
            )
            db_obj.categories.append(id_category)

        await session.commit()
        return db_obj


product_crud = ProductCrud(Product)
