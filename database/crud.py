from sqlalchemy import select, delete, or_, and_, update

from database.base import BaseAccessor
from database.dataclasses import WorkerDC
from database.models import Worker


class WorkersAccessor(BaseAccessor):
    async def get_all_filtered_by_name_surname(
        self, name: str | None = None, surname: str | None = None, **kwargs
    ) -> list[WorkerDC]:
        if name and surname:
            stmt = select(Worker).where(
                and_(Worker.name.ilike(name), Worker.surname.ilike(surname))
            )
        else:
            val = name or surname
            stmt = select(Worker).where(
                or_(Worker.name.ilike(f"{val}%"), Worker.surname.ilike(f"{val}%"))
            )
        res = (await self.session.scalars(stmt)).all()
        return [i.as_dataclass() for i in res]

    async def get_all(
        self, *args, **kwargs
    ) -> list[WorkerDC]:
        stmt = select(Worker)
        res = (await self.session.scalars(stmt)).all()
        return [i.as_dataclass() for i in res]

    async def get(self, **kwargs) -> WorkerDC:
        stmt = select(Worker).filter_by(**kwargs)
        res = await self.session.scalar(stmt)
        return res.as_dataclass()

    async def add(
        self,
        name: str,
        surname: str,
        position: str,
        project: str,
        patronymic: str = None,
    ) -> WorkerDC:
        to_db = Worker(
            name=name,
            surname=surname,
            position=position,
            project=project,
            patronymic=patronymic,
        )
        self.session.add(to_db)
        await self.session.flush()
        res = to_db.as_dataclass()
        await self.session.commit()
        return res

    async def update(self, worker_id: int, **kwargs) -> WorkerDC:
        stmt = (
            update(Worker)
            .where(Worker.id == worker_id)
            .values(**kwargs)
            .returning(Worker)
        )
        res = await self.session.scalar(stmt)
        res = res.as_dataclass()
        await self.session.commit()
        return res

    async def delete(self, worker_id: int) -> WorkerDC:
        stmt = delete(Worker).where(Worker.id == worker_id).returning(Worker)
        res = await self.session.scalar(stmt)
        res = res.as_dataclass()
        await self.session.commit()
        return res
