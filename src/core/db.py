from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker, declared_attr
# from sqlalchemy
from config import settings


class PreBase:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()


Base = declarative_base(cls = PreBase)

engine = create_async_engine(settings.db_url)

AsyncSessionLocal = sessionmaker(engine, class_= AsyncSession)


async def get_async_session():
    async with AsyncSessionLocal() as async_session:
        yield async_session
