from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from database.crud.crud import WorkersAccessor
from handlers.decorators import get_accessor
from handlers.states import FindWorker
from handlers.user.get.utils import handle_data
from keyboards.constants import SEARCH_BY_POSITION, NOT_FOUND, SEARCH_BY_PROJECT
from keyboards.utils import get_objects_keyboard

router = Router()


@router.callback_query(FindWorker.waiting_for_project, F.data.startswith("search:"))
@get_accessor(WorkersAccessor)
async def search_get_data(
    callback: CallbackQuery, state: FSMContext, accessor: WorkersAccessor
):
    data = callback.data.split(":")[-1]
    results = await accessor.get_all(project=data)
    await callback.answer(text="Результаты поиска:")
    await handle_data(message=callback.message, state=state, results=results)


@router.callback_query(FindWorker.waiting_for_project, F.data.startswith("search"))
async def search_search_projects(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text=SEARCH_BY_PROJECT)
    await state.set_state(FindWorker.search_project)
    await callback.answer()


@router.message(FindWorker.search_project)
@get_accessor(WorkersAccessor)
async def search_browse_projects(
    message: Message, state: FSMContext, accessor: WorkersAccessor
):
    data = message.text
    projects = await accessor.get_all_projects(project=data)
    await message.answer(
        text="Результаты поиска" if projects else NOT_FOUND,
        reply_markup=get_objects_keyboard(projects),
    )
    await state.set_state(FindWorker.waiting_for_project)


@router.callback_query(
    FindWorker.waiting_for_command, F.data.startswith("search:project")
)
@get_accessor(WorkersAccessor)
async def search_wait_for_command(
    callback: CallbackQuery, state: FSMContext, accessor: WorkersAccessor
):
    all_projects = await accessor.get_all_projects()
    keyboard = get_objects_keyboard(all_projects)
    await state.update_data(keyboard=keyboard)
    await callback.message.answer(text=SEARCH_BY_PROJECT, reply_markup=keyboard)
    await state.set_state(FindWorker.waiting_for_project)
    await callback.answer()
