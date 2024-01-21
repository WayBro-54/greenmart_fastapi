from fastapi.encoders import jsonable_encoder
from sqlalchemy.ext.asyncio import AsyncSession

from core.crud import CRUDBase
from .models import Agent


class AgentCRUD(CRUDBase):

    async def create_agent(
        self,
        obj_in,
        user_id: int,
        session: AsyncSession,
    ):
        obj_in_data = jsonable_encoder(obj_in)
        obj_in_data['user_id'] = user_id
        db_obj = self.model(**obj_in_data)

        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)

        return db_obj


agent_crud = AgentCRUD(Agent)
