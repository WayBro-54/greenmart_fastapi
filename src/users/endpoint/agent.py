from fastapi import APIRouter

agent_router = APIRouter()


@agent_router.get(
    '/',
)
async def get_user(self):



@agent_router.get('/orders')
async def get_orders(self):
    pass


@agent_router.patch('/')
async def get_orders():
    pass
