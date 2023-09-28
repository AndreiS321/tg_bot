from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

START_MESSAGE = "Для вызова меню помощи введите /помощь"
ADMIN_MESSAGE = "Режим администратора"
USER_MESSAGE = "Режим пользователя"
HELP_MESSAGE = (
    "Для поиска сотрудника введите /найти\n"
    "Для вывода списка всех сотрудников введите /все_сотрудники\n"
    "Для повторного вызова меню введите /меню\n"
    "Для отмены операции введите /отмена (отменяет просмотр результатов поиска)"
)
SEARCH_MESSAGE = "Выберите способ поиска"
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
UPDATE_DATE_MESSAGE = "Введите новую дату в формате (дд.мм.гггг)"

DELETE_WORKER_SUCCESS = "Сотрудник удалён"
DELETE_WORKER_QUESTION = "Вы уверены?"

SUCCESS_MESSAGE = "Сотрудник добавлен"
USER_NOT_EXIST = "Сотрудник удалён или не существует"
NOT_FOUND = "По результатам запроса ничего не найдено"
SEARCH_BY_NAME = "Введите имя и/или фамилию сотрудника"
SEARCH_BY_POSITION = "Выберите должность"
SEARCH_POSITION = "Введите должность для поиска"
SEARCH_BY_PROJECT = "Выберите проект"
SEARCH_PROJECT = "Введите название проекта для поиска"
SEARCH_BY_DATE_FROM = "Введите начальную дату в формате (дд.мм.гггг)"
SEARCH_BY_DATE_TO = "Введите конечную дату в формате (дд.мм.гггг)"
WRONG_DATE = (
    "Введите корректную дату в формате (дд.мм.гггг) или введите /отмена для выхода"
)
MENU_KEYBOARD = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="/найти"),
            KeyboardButton(text="/добавить"),
        ],
        [KeyboardButton(text="/все_сотрудники")],
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

SEARCH_KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="По имени и/или фамилии", callback_data="search:name"
            ),
            InlineKeyboardButton(text="По дате приёма", callback_data="search:date"),
            InlineKeyboardButton(text="По должности", callback_data="search:position"),
            InlineKeyboardButton(text="По проекту", callback_data="search:project"),
        ],
    ]
)

SEARCH_BY_PROJECT_KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="По проекту", callback_data="search:project:find"
            ),
            InlineKeyboardButton(
                text="По посмотреть", callback_data="search:project:all"
            ),
        ],
    ]
)
SEARCH_ROW = [
    InlineKeyboardButton(text="Найти по списку", callback_data="search:find"),
]
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
