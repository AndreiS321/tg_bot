from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from database.dataclasses import WorkerDC
from database.models import Worker
from keyboards.client import get_worker_keyboard


async def send_worker(message: Message, worker: WorkerDC):
    keyboard = get_worker_keyboard(worker)
    photo = Worker.get_image(worker.id)

    await message.answer_photo(photo=photo, reply_markup=keyboard)


async def save_prev_state(state: FSMContext):
    cur_state = await state.get_state()
    await state.update_data(prev_state=cur_state)


async def load_prev_state(state: FSMContext, clear_if_update_state: bool = True):
    data = await state.get_data()
    prev_state = data["prev_state"]
    if clear_if_update_state and (prev_state and prev_state.startswith("UpdateWorker")):
        prev_state = None
    await state.set_state(prev_state)
