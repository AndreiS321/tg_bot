from datetime import date

from sqlalchemy import select, delete, or_, and_, update

from database.base import BaseAccessor
from database.dataclasses import WorkerDC
from database.models import Worker


class WorkersAccessor(BaseAccessor):
    model = Worker
    model_dc = WorkerDC

    async def get_all_filtered_by_name_or_surname(
        self, name: str | None = None, surname: str | None = None, **kwargs
    ) -> list[model_dc]:
        if name and surname:
            stmt = select(self.model).where(
                and_(self.model.name.ilike(name), self.model.surname.ilike(surname))
            )
        else:
            val = name or surname
            stmt = select(self.model).where(
                or_(
                    self.model.name.ilike(f"{val}%"),
                    self.model.surname.ilike(f"{val}%"),
                )
            )
        res = (await self.session.scalars(stmt)).all()
        return [i.as_dataclass() for i in res]

    async def get_all_between_dates(
        self, date_from: date, date_to: date
    ) -> list[model_dc]:
        stmt = select(self.model).where(
            and_(
                date_to >= self.model.created_date, self.model.created_date >= date_from
            )
        )
        res = (await self.session.scalars(stmt)).all()
        return [i.as_dataclass() for i in res]

    async def get_all_by_position(self, position: str) -> list[model_dc]:
        stmt = select(self.model).where(self.model.position.ilike(position))
        res = (await self.session.scalars(stmt)).all()
        return [i.as_dataclass() for i in res]

    async def get_all_by_project(self, project: str) -> list[model_dc]:
        stmt = select(self.model).where(self.model.project.ilike(project))
        res = (await self.session.scalars(stmt)).all()
        return [i.as_dataclass() for i in res]

    async def get_all_positions(
        self, *args, position: str = None, **kwargs
    ) -> list[str]:
        stmt = select(self.model.position).distinct(self.model.position)
        if position:
            stmt = stmt.where(self.model.position.ilike(position))
        res = (await self.session.scalars(stmt)).all()
        return res

    async def get_all_projects(self, *args, project: str = None, **kwargs) -> list[str]:
        stmt = select(self.model.project).distinct(self.model.project)
        if project:
            stmt = stmt.where(self.model.project.ilike(project))
        res = (await self.session.scalars(stmt)).all()
        return res
