from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from bot import Bot
from database.crud import WorkersAccessor
from database.models import Worker
from handlers.decorators import get_accessor
from handlers.states import AddWorker
from keyboards.constants import (
    ADD_NAME_MESSAGE,
    ADD_SURNAME_MESSAGE,
    ADD_PATRONYMIC_MESSAGE,
    ADD_POSITION_MESSAGE,
    ADD_PROJECT_MESSAGE,
    OPTIONAL_KEYBOARD,
    SUCCESS_MESSAGE,
    ADD_IMAGE_MESSAGE,
)

router = Router()


@router.callback_query(AddWorker.waiting_for_image, F.data == "add:pass")
@get_accessor(WorkersAccessor)
async def add_worker_no_image(
    message: CallbackQuery, state: FSMContext, accessor: WorkersAccessor
):
    data = await state.get_data()
    await accessor.add(
        name=data["name"],
        surname=data["surname"],
        patronymic=data["patronymic"],
        position=data["position"],
        project=data["project"],
    )
    await message.message.answer(text=SUCCESS_MESSAGE)
    await state.clear()
    await message.answer()


@router.message(AddWorker.waiting_for_image)
@get_accessor(WorkersAccessor)
async def add_worker_image(
    message: Message, state: FSMContext, accessor: WorkersAccessor, bot: Bot
):
    data = await state.get_data()
    new_worker = await accessor.add(
        name=data["name"],
        surname=data["surname"],
        patronymic=data["patronymic"],
        position=data["position"],
        project=data["project"],
    )
    photo_url = Worker.get_image_url(new_worker.id).absolute()
    photo_url.unlink(missing_ok=True)
    if message.photo:
        await bot.download(file=message.photo[-1], destination=photo_url)
    await message.answer(text=SUCCESS_MESSAGE)
    await state.clear()


@router.message(AddWorker.waiting_for_project)
async def add_worker_project(message: Message, state: FSMContext):
    await state.update_data(project=message.text)
    await message.answer(text=ADD_IMAGE_MESSAGE, reply_markup=OPTIONAL_KEYBOARD)
    await state.set_state(AddWorker.waiting_for_image)


@router.message(AddWorker.waiting_for_position)
async def add_worker_position(message: Message, state: FSMContext):
    await state.update_data(position=message.text)
    await message.answer(text=ADD_PROJECT_MESSAGE)
    await state.set_state(AddWorker.waiting_for_project)


@router.callback_query(AddWorker.waiting_for_patronymic, F.data == "add:pass")
async def add_worker_no_patronymic(message: CallbackQuery, state: FSMContext):
    await state.update_data(patronymic=None)
    await message.message.answer(text=ADD_POSITION_MESSAGE)
    await state.set_state(AddWorker.waiting_for_position)
    await message.answer()


@router.message(AddWorker.waiting_for_patronymic)
async def add_worker_patronymic(message: Message, state: FSMContext):
    await state.update_data(patronymic=message.text)
    await message.answer(text=ADD_POSITION_MESSAGE)
    await state.set_state(AddWorker.waiting_for_position)


@router.message(AddWorker.waiting_for_surname)
async def add_worker_surname(message: Message, state: FSMContext):
    await state.update_data(surname=message.text)
    await message.answer(text=ADD_PATRONYMIC_MESSAGE, reply_markup=OPTIONAL_KEYBOARD)
    await state.set_state(AddWorker.waiting_for_patronymic)


@router.message(AddWorker.waiting_for_name)
async def add_worker_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(text=ADD_SURNAME_MESSAGE)
    await state.set_state(AddWorker.waiting_for_surname)


@router.message(Command("добавить"))
async def add_worker_start(message: Message, state: FSMContext):
    await message.answer(text=ADD_NAME_MESSAGE)
    await state.set_state(AddWorker.waiting_for_name)
