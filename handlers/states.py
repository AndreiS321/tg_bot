from aiogram.fsm.state import StatesGroup, State


class FindWorker(StatesGroup):
    waiting_for_command = State()

    waiting_for_name = State()
    waiting_for_position = State()
    waiting_for_project = State()
    waiting_for_date_from = State()
    waiting_for_date_to = State()

    search_position = State()
    search_project = State()

    browsing_results = State()
    browsing_projects = State()
    browsing_positions = State()


class AddWorker(StatesGroup):
    waiting_for_name = State()
    waiting_for_surname = State()
    waiting_for_patronymic = State()

    waiting_for_position = State()
    waiting_for_project = State()
    waiting_for_image = State()


class UpdateWorker(StatesGroup):
    waiting_for_name = State()
    waiting_for_surname = State()
    waiting_for_patronymic = State()

    waiting_for_position = State()
    waiting_for_project = State()
    waiting_for_image = State()
    waiting_for_date = State()


class DeleteWorker(StatesGroup):
    waiting_for_confirm = State()
