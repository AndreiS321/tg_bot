from datetime import date

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from database.crud.crud import WorkersAccessor
from handlers.decorators import get_accessor
from handlers.states import FindWorker
from handlers.user.get.utils import handle_data
from handlers.utils import to_date
from keyboards.constants import SEARCH_BY_DATE_FROM, SEARCH_BY_DATE_TO, WRONG_DATE

router = Router()


@router.message(FindWorker.waiting_for_date_to)
@get_accessor(WorkersAccessor)
async def search_get_data(
    message: Message, state: FSMContext, accessor: WorkersAccessor
):
    date_to = to_date(message.text)
    if not date_to:
        await message.answer(text=WRONG_DATE)
        return None
    data = await state.get_data()
    date_from = data["date_from"]
    results = await accessor.get_all_between_dates(date_from=date_from, date_to=date_to)
    await message.answer(text="Результаты поиска:")
    await handle_data(message=message, state=state, results=results)


@router.message(FindWorker.waiting_for_date_from)
async def search_get_date_from(message: Message, state: FSMContext):
    date_from = to_date(message.text)
    if not date_from:
        await message.answer(text=WRONG_DATE)
        return None
    await state.update_data(date_from=date_from)
    await message.answer(text=SEARCH_BY_DATE_TO)
    await state.set_state(FindWorker.waiting_for_date_to)


@router.callback_query(FindWorker.waiting_for_command, F.data.startswith("search:date"))
async def search_wait_for_command(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text=SEARCH_BY_DATE_FROM)
    await state.set_state(FindWorker.waiting_for_date_from)
    await callback.answer()
