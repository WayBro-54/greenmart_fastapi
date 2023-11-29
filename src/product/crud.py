import asyncio
from fastapi.encoders import jsonable_encoder
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

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
        obj_in_data = jsonable_encoder(obj_in)
        categories = obj_in_data.pop('categories')
        db_obj = self.model(**obj_in_data)
        session.add(db_obj)

        await session.commit()
        await session.refresh(db_obj, ['categories'])
        print(categories)
        for category in categories:
            id_category = await GET_CATEGORY['id'](category['id'], session)
            print(id_category)
            # if category['id'] and GET_CATEGORY['id'](category['id'], session) is not None:
            #     id_category = GET_CATEGORY['id'](category['id'], session)
            # elif category['title'] and GET_CATEGORY['title'](category['title'], session) is not None:
            #     id_category = GET_CATEGORY['title'](category['title'], session)
            # elif category['code'] and GET_CATEGORY['code'](category['code'], session) is not None:
            #     id_category = GET_CATEGORY['code'](category.code, session)
            db_obj.categories.append(id_category)
        await session.commit()
        return db_obj


product_crud = ProductCrud(Product)
