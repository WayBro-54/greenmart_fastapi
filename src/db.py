from typing import Dict, Any
from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base, declared_attr

from config import settings


class PreBase:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    def __repr__(self) -> str:
        params = ", ".join(
            f"{attr}={value!r}"
            for attr, value in self.__dict__.items()
            if not attr.startswith("_")
        )
        return f"{type(self).__name__}({params})"

    def as_dict(self) -> Dict[str, Any]:
        return {
            attr: value
            for attr, value in self.__dict__.items()
            if not attr.startswith("_")
        }


Base = declarative_base(cls=PreBase)

metadata = MetaData()

engine = create_async_engine(settings.db_url, echo=True, future=True)

AsyncSessionLocal = async_sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession
)


async def get_async_session():
    async with AsyncSessionLocal() as async_session:
        yield async_session
