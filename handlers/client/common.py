from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from database.crud import WorkersAccessor
from handlers.decorators import get_accessor
from handlers.states import FindWorker
from keyboards.constants import START_MESSAGE, HELP_MESSAGE, MENU_KEYBOARD

router = Router()


@router.callback_query(F.data == "no_data")
async def common_callback(message: CallbackQuery):
    await message.answer()


@router.message()
async def common_message(message: Message) -> None:
    await message.answer(text=HELP_MESSAGE, reply_markup=MENU_KEYBOARD)
