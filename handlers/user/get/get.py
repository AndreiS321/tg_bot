from aiogram import Router, F
from aiogram.filters import Command, or_f
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, InputMediaPhoto


from database.models import Worker
from handlers.decorators import get_accessor
from handlers.states import FindWorker
from keyboards.utils import get_worker_keyboard
from keyboards.constants import (
    SEARCH_MESSAGE,
    NOT_FOUND_MESSAGE,
    SEARCH_PAGINATION_ROW,
    SEARCH_PAGINATION_ROW_ONLY_PREV,
    SEARCH_PAGINATION_ROW_ONLY_NEXT,
    SEARCH_KEYBOARD,
)

router = Router()


@router.callback_query(FindWorker.browsing_results, F.data == "search:prev")
async def search_prev(message: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    results = data["results"]
    cursor = data["cursor"] - 1
    cur_worker = results[cursor]
    photo = InputMediaPhoto(media=Worker.get_image(cur_worker.id))
    keyboard = get_worker_keyboard(cur_worker)
    if cursor > 0:
        keyboard.inline_keyboard.append(SEARCH_PAGINATION_ROW)
    else:
        keyboard.inline_keyboard.append(SEARCH_PAGINATION_ROW_ONLY_NEXT)

    await message.message.edit_media(photo, reply_markup=keyboard)
    await state.update_data(cursor=cursor)
    await message.answer()


@router.callback_query(FindWorker.browsing_results, F.data == "search:next")
async def search_next(message: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    results = data["results"]
    cursor = data["cursor"] + 1
    res_count = data["res_count"]
    cur_worker = results[cursor]
    photo = InputMediaPhoto(media=Worker.get_image(cur_worker.id))
    keyboard = get_worker_keyboard(cur_worker)
    if cursor < res_count - 1:
        keyboard.inline_keyboard.append(SEARCH_PAGINATION_ROW)
    else:
        keyboard.inline_keyboard.append(SEARCH_PAGINATION_ROW_ONLY_PREV)

    await message.message.edit_media(photo, reply_markup=keyboard)
    await state.update_data(cursor=cursor)
    await message.answer()


@router.message(Command("найти"))
async def search_start(message: Message, state: FSMContext) -> None:
    await message.answer(text=SEARCH_MESSAGE, reply_markup=SEARCH_KEYBOARD)
    await state.clear()
    await state.set_state(FindWorker.waiting_for_command)
