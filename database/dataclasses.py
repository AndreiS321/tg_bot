from dataclasses import dataclass
from datetime import datetime

from aiogram.types import FSInputFile


@dataclass
class WorkerDC:
    id: int
    name: str
    surname: str
    position: str
    project: str
    created_date: datetime

    image: FSInputFile

    patronymic: str | None = None


@dataclass
class AdminDC:
    id: int
    tg_id: int
