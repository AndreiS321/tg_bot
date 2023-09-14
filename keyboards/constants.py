from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

START_MESSAGE = "Для вызова меню помощи введите /помощь"
HELP_MESSAGE = "Для поиска сотрудника введите /найти\nДля повторного вызова меню введите /меню\nДля отмены операции введите /отмена (отменяет просмотр результатов поиска)"
SEARCH_MESSAGE = "Введите имя и/или фамилию сотрудника"
CANCEL_MESSAGE = "Операция отменена"
UNKNOWN_COMMAND_MESSAGE = "Операция отменена"

NOT_FOUND_MESSAGE = "По результатам поиска такого сотрудника не найдено"

ADD_NAME_MESSAGE = "Введите имя нового сотрудника"
ADD_SURNAME_MESSAGE = "Введите фамилию нового сотрудника"
ADD_PATRONYMIC_MESSAGE = "Введите отчество нового сотрудника"
ADD_POSITION_MESSAGE = "Введите должность нового сотрудника"
ADD_PROJECT_MESSAGE = "Введите проект нового сотрудника"
ADD_IMAGE_MESSAGE = "Загрузите фотографию сотрудника"

UPDATE_NAME_MESSAGE = "Введите новое имя сотрудника"
UPDATE_SURNAME_MESSAGE = "Введите новою фамилию сотрудника"
UPDATE_PATRONYMIC_MESSAGE = "Введите новое отчество сотрудника"
UPDATE_POSITION_MESSAGE = "Введите новую должность сотрудника"
UPDATE_PROJECT_MESSAGE = "Введите новый проект сотрудника"
UPDATE_IMAGE_MESSAGE = "Загрузите новую фотографию сотрудника"

DELETE_WORKER_SUCCESS = "Сотрудник удалён"
DELETE_WORKER_QUESTION = "Вы уверены?"

SUCCESS_MESSAGE = "Сотрудник добавлен"

MENU_KEYBOARD = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="/найти"),
            KeyboardButton(text="/добавить"),
        ],
        [KeyboardButton(text="/помощь")],
        [KeyboardButton(text="/отмена")],
    ],
    resize_keyboard=True,
)

OPTIONAL_KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Пропустить", callback_data="add:pass"),
        ],
    ]
)

CONFIRM_DELETE_KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Подтвердить", callback_data="delete_yes"),
            InlineKeyboardButton(text="Отменить", callback_data="delete_no"),
        ],
    ]
)
SEARCH_PAGINATION_ROW = [
    InlineKeyboardButton(text="<<", callback_data="search:prev"),
    InlineKeyboardButton(text=">>", callback_data="search:next"),
]
SEARCH_PAGINATION_ROW_ONLY_NEXT = [
    InlineKeyboardButton(text=">>", callback_data="search:next"),
]
SEARCH_PAGINATION_ROW_ONLY_PREV = [
    InlineKeyboardButton(text="<<", callback_data="search:prev"),
]
