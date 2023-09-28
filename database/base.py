from typing import Optional

from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from bot import bot


class BaseAccessor:
    model = None
    model_dc = None

    def __init__(self):
        self.session: AsyncSession = bot.db.session_maker()

    async def get_all(self, *args, **kwargs) -> list[model]:
        stmt = select(self.model).filter_by(**kwargs)
        res = (await self.session.scalars(stmt)).all()
        return [i.as_dataclass() for i in res]

    async def get(self, **kwargs) -> Optional[model_dc]:
        stmt = select(self.model).filter_by(**kwargs)
        res = await self.session.scalar(stmt)
        if not res:
            return None
        return res.as_dataclass()

    async def add(self, *args, **kwargs) -> model_dc:
        to_db = self.model(
            **kwargs,
        )
        self.session.add(to_db)
        await self.session.flush()
        res = to_db.as_dataclass()
        await self.session.commit()
        return res

    async def update(self, record_id: int, **kwargs) -> Optional[model_dc]:
        stmt = (
            update(self.model)
            .where(self.model.id == record_id)
            .values(**kwargs)
            .returning(self.model)
        )
        res = await self.session.scalar(stmt)
        if not res:
            return None
        res = res.as_dataclass()
        await self.session.commit()
        return res

    async def delete(self, record_id: int) -> model_dc:
        stmt = (
            delete(self.model).where(self.model.id == record_id).returning(self.model)
        )
        res = await self.session.scalar(stmt)
        if not res:
            return None
        res = res.as_dataclass()
        await self.session.commit()
        return res
