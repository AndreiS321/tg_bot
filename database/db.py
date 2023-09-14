from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from config import DatabaseConfig


class Database:
    def __init__(self):
        self.engine = create_async_engine(
            f"postgresql+asyncpg://"
            f"{DatabaseConfig.user}:{DatabaseConfig.password}@"
            f"{DatabaseConfig.host}:{DatabaseConfig.port}/{DatabaseConfig.name}"
        )
        self.session_maker = async_sessionmaker(self.engine, class_=AsyncSession)

    def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        with self.session_maker.begin() as session:
            yield session
