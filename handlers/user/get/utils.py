from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from database.dataclasses import WorkerDC
from handlers.states import FindWorker
from keyboards.utils import get_worker_keyboard
from keyboards.constants import SEARCH_PAGINATION_ROW_ONLY_NEXT, NOT_FOUND_MESSAGE


async def handle_data(
    message: Message, state: FSMContext, results: list[WorkerDC] | None
):
    if results:
        worker = results[0]
        keyboard = get_worker_keyboard(worker)
        if len(results) > 1:
            keyboard.inline_keyboard.append(SEARCH_PAGINATION_ROW_ONLY_NEXT)
            await state.update_data(results=results)
            res_count = len(results)
            await state.update_data(res_count=res_count)
            await state.update_data(cursor=0)
            await state.set_state(FindWorker.browsing_results)
        else:
            await state.clear()
        await message.answer_photo(photo=worker.image, reply_markup=keyboard)
    else:
        await message.answer(text=NOT_FOUND_MESSAGE)
        await state.clear()
