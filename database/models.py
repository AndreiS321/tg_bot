import os
from datetime import date
from pathlib import Path

from aiogram.types import FSInputFile
from sqlalchemy import String, Date, func, Integer
from sqlalchemy.orm import mapped_column, Mapped

from database.dataclasses import WorkerDC, AdminDC
from database.decl_base import db

DEFAULT_IMAGE_PATH = os.path.abspath(Path(f"media/users/workers_avatars/default.png"))


class Worker(db):
    __tablename__ = "worker"
    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(String(255))
    surname: Mapped[str] = mapped_column(String(255))
    patronymic: Mapped[str] = mapped_column(String(255), nullable=True)

    position: Mapped[str] = mapped_column(String(255))
    project: Mapped[str] = mapped_column(String(255))
    created_date: Mapped[date] = mapped_column(Date(), server_default=func.now())

    @property
    def image(self) -> FSInputFile:
        return self.get_image(self.id)

    @staticmethod
    def get_image(img_id: int) -> FSInputFile:
        path = Path(f"media/users/workers_avatars/{img_id}.png")
        path = path if os.path.exists(path) else DEFAULT_IMAGE_PATH
        return FSInputFile(path)

    @staticmethod
    def get_image_url(img_id: int):
        path = Path(f"media/users/workers_avatars/{img_id}.png")
        return path

    def as_dataclass(self) -> WorkerDC:
        return WorkerDC(
            id=self.id,
            name=self.name,
            surname=self.surname,
            patronymic=self.patronymic,
            position=self.position,
            project=self.project,
            created_date=self.created_date,
            image=self.image,
        )


class Admin(db):
    __tablename__ = "admin"
    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[int] = mapped_column(Integer())

    def as_dataclass(self) -> AdminDC:
        return AdminDC(id=self.id, tg_id=self.tg_id)
