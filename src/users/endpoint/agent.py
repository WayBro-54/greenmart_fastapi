from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from users.config import current_user
from users.models import Users

from db import get_async_session
from users.crud import agent_crud
from users.shemas import AgentCreate

agent_router = APIRouter()


@agent_router.get(
    '/',
)
async def get_user(
        user: Users = Depends(current_user),
        session: AsyncSession = Depends(get_async_session),
):


    pass


@agent_router.get('/orders')
async def get_orders():
    pass


@agent_router.post('/me')
async def agent_create(
    obj_data: AgentCreate,
    user: Users = Depends(current_user),
    session: AsyncSession = Depends(get_async_session)
):
    agent_data = await agent_crud.create_agent(
        obj_data,
        user.id,
        session,
    )

    return agent_data
