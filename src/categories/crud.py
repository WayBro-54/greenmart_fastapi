from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.encoders import jsonable_encoder

from core.crud import CRUDBase
from categories.models import Categories


class CategoriesCRUD(CRUDBase):
    pass


category_crud = CategoriesCRUD(Categories)
