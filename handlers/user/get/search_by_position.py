from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from database.crud.crud import WorkersAccessor
from handlers.decorators import get_accessor
from handlers.states import FindWorker
from handlers.user.get.utils import handle_data
from keyboards.constants import SEARCH_BY_POSITION, NOT_FOUND, SEARCH_POSITION
from keyboards.utils import get_objects_keyboard

router = Router()


@router.callback_query(FindWorker.waiting_for_position, F.data.startswith("search:"))
@get_accessor(WorkersAccessor)
async def search_get_data(
    callback: CallbackQuery, state: FSMContext, accessor: WorkersAccessor
):
    data = callback.data.split(":")[-1]
    results = await accessor.get_all(position=data)
    await callback.answer(text="Результаты поиска:")
    await handle_data(message=callback.message, state=state, results=results)


@router.callback_query(FindWorker.waiting_for_position, F.data.startswith("search"))
async def search_search_positions(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text=SEARCH_POSITION)
    await state.set_state(FindWorker.search_position)
    await callback.answer()


@router.message(FindWorker.search_position)
@get_accessor(WorkersAccessor)
async def search_browse_positions(
    message: Message, state: FSMContext, accessor: WorkersAccessor
):
    data = message.text
    positions = await accessor.get_all_positions(position=data)
    await message.answer(
        text="Результаты поиска" if positions else NOT_FOUND,
        reply_markup=get_objects_keyboard(positions),
    )
    await state.set_state(FindWorker.waiting_for_position)


@router.callback_query(
    FindWorker.waiting_for_command, F.data.startswith("search:position")
)
@get_accessor(WorkersAccessor)
async def search_wait_for_command(
    callback: CallbackQuery, state: FSMContext, accessor: WorkersAccessor
):
    all_positions = await accessor.get_all_positions()
    keyboard = get_objects_keyboard(all_positions)
    await state.update_data(keyboard=keyboard)
    await callback.message.answer(text=SEARCH_BY_POSITION, reply_markup=keyboard)
    await state.set_state(FindWorker.waiting_for_position)
    await callback.answer()
