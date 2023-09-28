from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from bot import Bot
from database.crud.crud import WorkersAccessor

from database.models import Worker
from handlers.admin.utils import send_worker, save_prev_state, load_prev_state
from handlers.decorators import get_accessor
from handlers.states import UpdateWorker
from handlers.utils import to_date
from keyboards.constants import (
    UPDATE_NAME_MESSAGE,
    UPDATE_SURNAME_MESSAGE,
    UPDATE_PATRONYMIC_MESSAGE,
    UPDATE_POSITION_MESSAGE,
    UPDATE_PROJECT_MESSAGE,
    UPDATE_IMAGE_MESSAGE,
    WRONG_DATE,
    UPDATE_DATE_MESSAGE,
)

router = Router()


@router.message(UpdateWorker.waiting_for_image)
@get_accessor(WorkersAccessor)
async def update_worker_image(
    message: Message, state: FSMContext, bot: Bot, accessor: WorkersAccessor
):
    data = await state.get_data()
    worker_id = int(data["worker_id_update"])
    cur_worker = await accessor.get(id=worker_id)

    if message.photo:
        photo_url = Worker.get_image_url(worker_id).absolute()
        photo_url.unlink(missing_ok=True)
        await bot.download(file=message.photo[-1], destination=photo_url)
    await send_worker(message, cur_worker)
    await load_prev_state(state)


@router.callback_query(F.data.startswith("update:image"))
async def update_worker_image_callback(message: CallbackQuery, state: FSMContext):
    await state.set_state(UpdateWorker.waiting_for_image)
    await save_prev_state(state)
    await state.update_data(worker_id_update=message.data.split(":")[-1])
    await message.message.answer(text=UPDATE_IMAGE_MESSAGE)
    await message.answer()


@router.message(UpdateWorker.waiting_for_project)
@get_accessor(WorkersAccessor)
async def update_worker_project(
    message: Message, state: FSMContext, accessor: WorkersAccessor
):
    project = message.text
    data = await state.get_data()
    worker_id = int(data["worker_id_update"])
    cur_worker = await accessor.update(record_id=worker_id, project=project)
    await send_worker(message, cur_worker)
    await load_prev_state(state)


@router.callback_query(F.data.startswith("update:project"))
async def update_worker_project_callback(message: CallbackQuery, state: FSMContext):
    await state.set_state(UpdateWorker.waiting_for_project)
    await save_prev_state(state)
    await state.update_data(worker_id_update=message.data.split(":")[-1])
    await message.message.answer(text=UPDATE_PROJECT_MESSAGE)
    await message.answer()


@router.message(UpdateWorker.waiting_for_position)
@get_accessor(WorkersAccessor)
async def update_worker_position(
    message: Message, state: FSMContext, accessor: WorkersAccessor
):
    position = message.text
    data = await state.get_data()
    worker_id = int(data["worker_id_update"])
    cur_worker = await accessor.update(record_id=worker_id, position=position)
    await send_worker(message, cur_worker)
    await load_prev_state(state)


@router.callback_query(F.data.startswith("update:position"))
async def update_worker_position_callback(message: CallbackQuery, state: FSMContext):
    await state.set_state(UpdateWorker.waiting_for_position)
    await save_prev_state(state)
    await state.update_data(worker_id_update=message.data.split(":")[-1])
    await message.message.answer(text=UPDATE_POSITION_MESSAGE)
    await message.answer()


@router.message(UpdateWorker.waiting_for_patronymic)
@get_accessor(WorkersAccessor)
async def update_worker_patronymic(
    message: Message, state: FSMContext, accessor: WorkersAccessor
):
    patronymic = message.text
    data = await state.get_data()
    worker_id = int(data["worker_id_update"])
    cur_worker = await accessor.update(record_id=worker_id, patronymic=patronymic)
    await send_worker(message, cur_worker)
    await load_prev_state(state)


@router.callback_query(F.data.startswith("update:patronymic"))
async def update_worker_patronymic_callback(message: CallbackQuery, state: FSMContext):
    await state.set_state(UpdateWorker.waiting_for_patronymic)
    await save_prev_state(state)
    await state.update_data(worker_id_update=message.data.split(":")[-1])
    await message.message.answer(text=UPDATE_PATRONYMIC_MESSAGE)
    await message.answer()


@router.message(UpdateWorker.waiting_for_surname)
@get_accessor(WorkersAccessor)
async def update_worker_surname(
    message: Message, state: FSMContext, accessor: WorkersAccessor
):
    surname = message.text
    data = await state.get_data()
    worker_id = int(data["worker_id_update"])
    cur_worker = await accessor.update(record_id=worker_id, surname=surname)
    await send_worker(message, cur_worker)
    await load_prev_state(state)


@router.callback_query(F.data.startswith("update:surname"))
async def update_worker_surname_callback(message: CallbackQuery, state: FSMContext):
    await state.set_state(UpdateWorker.waiting_for_surname)
    await save_prev_state(state)
    await state.update_data(worker_id_update=message.data.split(":")[-1])
    await message.message.answer(text=UPDATE_SURNAME_MESSAGE)
    await message.answer()


@router.message(UpdateWorker.waiting_for_name)
@get_accessor(WorkersAccessor)
async def update_worker_name(
    message: Message, state: FSMContext, accessor: WorkersAccessor
):
    name = message.text
    data = await state.get_data()
    worker_id = int(data["worker_id_update"])
    cur_worker = await accessor.update(record_id=worker_id, name=name)
    await send_worker(message, cur_worker)
    await load_prev_state(state)


@router.callback_query(F.data.startswith("update:name"))
async def update_worker_name_callback(message: CallbackQuery, state: FSMContext):
    await state.set_state(UpdateWorker.waiting_for_name)
    await save_prev_state(state)
    await state.update_data(worker_id_update=message.data.split(":")[-1])
    await message.message.answer(text=UPDATE_NAME_MESSAGE)
    await message.answer()


@router.message(UpdateWorker.waiting_for_date)
@get_accessor(WorkersAccessor)
async def update_worker_date(
    message: Message, state: FSMContext, accessor: WorkersAccessor
):
    date = to_date(message.text)
    if not date:
        await message.answer(text=WRONG_DATE)
        return None
    data = await state.get_data()
    worker_id = int(data["worker_id_update"])
    cur_worker = await accessor.update(record_id=worker_id, created_date=date)
    await send_worker(message, cur_worker)
    await load_prev_state(state)


@router.callback_query(F.data.startswith("update:date"))
async def update_worker_date_callback(callback: CallbackQuery, state: FSMContext):
    await state.set_state(UpdateWorker.waiting_for_date)
    await save_prev_state(state)
    await state.update_data(worker_id_update=callback.data.split(":")[-1])
    await callback.message.answer(text=UPDATE_DATE_MESSAGE)
    await callback.answer()
