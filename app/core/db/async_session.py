from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.engine import make_url
from sqlalchemy.pool import NullPool

from app.core.config import settings


database_url = settings.database_url
url = make_url(database_url)

engine_kwargs = {
    "future": True,
    "echo": settings.debug,
}

if url.get_backend_name().startswith("sqlite"):
    engine_kwargs["poolclass"] = NullPool
else:
    engine_kwargs.update(
        {
            "pool_pre_ping": True,
            "pool_size": 5,
            "max_overflow": 10,
            "pool_timeout": 30,
        }
    )

engine = create_async_engine(
    database_url,
    **engine_kwargs,
)

async_session = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

async def get_async_db() -> AsyncSession:
    async with async_session() as session:
        yield session
