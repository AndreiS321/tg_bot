from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from database.crud import WorkersAccessor
from handlers.decorators import get_accessor
from handlers.states import FindWorker
from keyboards.constants import START_MESSAGE, HELP_MESSAGE, MENU_KEYBOARD

router = Router()


# @router.message(Command("найти"))
# @get_accessor(WorkersAccessor)
# async def search(message: Message, state: FSMContext, accessor: WorkersAccessor) -> None:
#     await message.answer(chat_id=message.chat.id)
#     await state.set_state(FindWorker.waiting_for_data)


# @router.message(FindWorker.waiting_for_data)
# @get_accessor(WorkersAccessor)
# async def help_msg(message: Message, state: FSMContext, accessor: WorkersAccessor):
#     data = message.text.split()
#     if len(data) == 2:
#         res = accessor.get(name=data[0],surname=data[1])
#     await message.answer(text=HELP_MESSAGE)


@router.callback_query(F.data == "no_data")
async def common_callback(message: CallbackQuery):
    await message.answer()


@router.message()
async def common_message(message: Message) -> None:
    await message.answer(text=HELP_MESSAGE, reply_markup=MENU_KEYBOARD)
