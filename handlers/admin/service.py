from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from database.crud.admin import AdminAccessor
from handlers.decorators import get_accessor
from keyboards.constants import (
    START_MESSAGE,
    MENU_KEYBOARD,
    HELP_MESSAGE,
    CANCEL_MESSAGE,
    ADMIN_MESSAGE,
    USER_MESSAGE,
)

router = Router()


@router.message(Command("admin"))
@get_accessor(AdminAccessor)
async def admin(message: Message, accessor: AdminAccessor):
    await accessor.add(tg_id=message.from_user.id)
    await message.answer(text=ADMIN_MESSAGE)


@router.message(Command("user"))
@get_accessor(AdminAccessor)
async def user(message: Message, accessor: AdminAccessor):
    admin = await accessor.get(tg_id=message.from_user.id)
    await accessor.delete(record_id=admin.id)
    await message.answer(text=USER_MESSAGE)


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
