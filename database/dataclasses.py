from dataclasses import dataclass
from datetime import date


@dataclass
class WorkerDC:
    id: int
    name: str
    surname: str
    position: str
    project: str
    created_date: date

    patronymic: str | None = None
