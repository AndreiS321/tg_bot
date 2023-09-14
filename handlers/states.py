from aiogram.fsm.state import StatesGroup, State


class FindWorker(StatesGroup):
    waiting_for_data = State()
    browsing_results = State()


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


class DeleteWorker(StatesGroup):
    waiting_for_confirm = State()
