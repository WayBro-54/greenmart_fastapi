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
    
    async def create(
        self,
        obj_in,
        session: AsyncSession,
    ):
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        session.add(db_obj)

        await session.commit()
        await session.refresh(db_obj)
        return db_obj

    async def update(
        self,
        obj_db,
        obj_in,
        session: AsyncSession,
    ):
        obj_data = jsonable_encoder(obj_db)
        update_data = jsonable_encoder(obj_in)

        for field in obj_data:
            if field in update_data:
                setattr(obj_db, field, update_data[field])

        session.add(obj_db)
        await session.commit()
        await session.refresh(obj_db)
        return obj_db

    async def remove(
          self,
          obj_db,
          session: AsyncSession,
    ):
        await session.delete(obj_db)
        await session.commit()
        return obj_db


