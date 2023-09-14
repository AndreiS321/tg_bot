from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from keyboards.constants import (
    START_MESSAGE,
    MENU_KEYBOARD,
    HELP_MESSAGE,
    CANCEL_MESSAGE,
)

router = Router()


@router.message(Command("отмена", ignore_case=True))
async def cancel(message: Message, state: FSMContext):
    await state.set_state(None)
    await message.answer(text=CANCEL_MESSAGE, reply_markup=MENU_KEYBOARD)


@router.message(Command("start", ignore_case=True))
async def start(message: Message):
    await message.answer(text=START_MESSAGE, reply_markup=MENU_KEYBOARD)


@router.message(Command("помощь", ignore_case=True))
async def help_msg(message: Message):
    await message.answer(text=HELP_MESSAGE, reply_markup=MENU_KEYBOARD)
