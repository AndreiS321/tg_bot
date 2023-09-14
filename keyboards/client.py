from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from database.dataclasses import WorkerDC


def get_worker_keyboard(worker_dc: WorkerDC) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=f"Имя: {worker_dc.name}",
                    callback_data=f"update:name:{worker_dc.id}",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=f"Фамилия: {worker_dc.surname}",
                    callback_data=f"update:surname:{worker_dc.id}",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=f"Отчество: {worker_dc.patronymic if worker_dc.patronymic else 'Не указано'}",
                    callback_data=f"update:patronymic:{worker_dc.id}",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=f"Должность: {worker_dc.position}",
                    callback_data=f"update:position:{worker_dc.id}",
                ),
                InlineKeyboardButton(
                    text=f"Проект: {worker_dc.project}",
                    callback_data=f"update:project:{worker_dc.id}",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=f"Дата записи: {worker_dc.created_date}",
                    callback_data="no_data",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=f"Обновить аватар",
                    callback_data=f"update:image:{worker_dc.id}",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=f"Удалить сотрудника", callback_data=f"delete:{worker_dc.id}"
                ),
            ],
        ]
    )
    return keyboard
