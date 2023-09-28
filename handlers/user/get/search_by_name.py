from aiogram import Router, F
from aiogram.filters import or_f, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from database.crud.crud import WorkersAccessor
from database.dataclasses import WorkerDC
from handlers.decorators import get_accessor
from handlers.states import FindWorker
from handlers.user.get.utils import handle_data
from keyboards.utils import get_worker_keyboard
from keyboards.constants import (
    SEARCH_PAGINATION_ROW_ONLY_NEXT,
    NOT_FOUND_MESSAGE,
    SEARCH_BY_NAME,
)

router = Router()


@router.message(Command("все_сотрудники"))
@get_accessor(WorkersAccessor)
async def get_all(message: Message, state: FSMContext, accessor: WorkersAccessor):
    results = await accessor.get_all()
    await message.answer(text="Результаты поиска:")
    await handle_data(message=message, state=state, results=results)


@router.message(FindWorker.waiting_for_name)
@get_accessor(WorkersAccessor)
async def search_get_data(
    message: Message, state: FSMContext, accessor: WorkersAccessor
):
    data = message.text.split()
    results = await accessor.get_all_filtered_by_name_or_surname(*data)
    await message.answer(text="Результаты поиска:")
    await handle_data(message=message, state=state, results=results)


@router.callback_query(FindWorker.waiting_for_command, F.data.startswith("search:name"))
async def search_wait_for_command(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text=SEARCH_BY_NAME)
    await state.set_state(FindWorker.waiting_for_name)
    await callback.answer()
