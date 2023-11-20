from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class CRUDBase:

    def __init__(self, model) -> None:
        self.model = model
    
    async def get(
                  self,
                  obj_id: int,
                  session: AsyncSession,
    ):
        db_obj = await session.execute(
            select(self.model).where(
                self.model.id == obj_id
            )
        )
        return db_obj.scalars().first()
    
    async def get_all(
                      self,
                      session: AsyncSession,
    ):
        db_objs = await session.execute(
            select(self.model)
        )
        return db_objs.scalars().all()
    
    async def create_obj(self):
        pass

    async def update_obj(self):
        pass
    async def remove_obj(self):
        pass