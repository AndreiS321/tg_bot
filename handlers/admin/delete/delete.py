from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from bot import Bot
from database.crud.crud import WorkersAccessor

from database.models import Worker
from handlers.admin.utils import send_worker, save_prev_state, load_prev_state
from handlers.decorators import get_accessor
from handlers.states import UpdateWorker, DeleteWorker
from keyboards.constants import (
    UPDATE_NAME_MESSAGE,
    UPDATE_SURNAME_MESSAGE,
    UPDATE_PATRONYMIC_MESSAGE,
    UPDATE_POSITION_MESSAGE,
    UPDATE_PROJECT_MESSAGE,
    UPDATE_IMAGE_MESSAGE,
    CANCEL_MESSAGE,
    DELETE_WORKER_QUESTION,
    DELETE_WORKER_SUCCESS,
    CONFIRM_DELETE_KEYBOARD,
    USER_NOT_EXIST,
)

router = Router()


@router.callback_query(
    DeleteWorker.waiting_for_confirm, F.data.startswith("delete_yes")
)
@get_accessor(WorkersAccessor)
async def delete_worker(
    message: CallbackQuery, state: FSMContext, accessor: WorkersAccessor
):
    data = await state.get_data()
    worker_id = int(data["worker_id_delete"])
    res = await accessor.delete(record_id=worker_id)
    photo_url = Worker.get_image_url(res.id).absolute()
    photo_url.unlink(missing_ok=True)
    await message.message.answer(text=DELETE_WORKER_SUCCESS if res else USER_NOT_EXIST)
    await load_prev_state(state)
    await message.answer()


@router.callback_query(DeleteWorker.waiting_for_confirm, F.data.startswith("delete_no"))
async def delete_worker_cancel(message: CallbackQuery, state: FSMContext):
    await message.message.answer(text=CANCEL_MESSAGE)
    await load_prev_state(state)
    await message.answer()


@router.callback_query(F.data.startswith("delete:"))
async def delete_worker_confirm(message: CallbackQuery, state: FSMContext):
    worker_id = message.data.split(":")[-1]
    await save_prev_state(state)
    await state.update_data(worker_id_delete=worker_id)
    await state.set_state(DeleteWorker.waiting_for_confirm)
    await message.message.answer(
        text=DELETE_WORKER_QUESTION, reply_markup=CONFIRM_DELETE_KEYBOARD
    )
    await message.answer()
