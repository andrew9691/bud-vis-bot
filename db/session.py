from collections.abc import Coroutine
from functools import wraps
from typing import Any

from pydantic import PostgresDsn
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

from app import settings


sqlalchemy_database_uri = PostgresDsn.build(
    scheme='postgresql+asyncpg',
    username=settings.PG_USER,
    password=settings.PG_PASSWORD,
    host=settings.PG_HOST,
    port=settings.PG_PORT,
    path=settings.PG_DB,
)

engine = create_async_engine(
    str(sqlalchemy_database_uri),
)

SessionLocal = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


def provide_session(func: Coroutine) -> Coroutine:
    @wraps(func)
    async def wrapper(*args: Any, **kwargs: Any) -> Any:
        async with SessionLocal() as session:
            return await func(session, *args, **kwargs)
    return wrapper
