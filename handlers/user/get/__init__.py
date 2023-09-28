from aiogram import Router

from handlers.user.get.get import router as get_router
from handlers.user.get.search_by_name import router as search_by_name_router
from handlers.user.get.search_by_date import router as search_by_date_router
from handlers.user.get.search_by_position import router as search_by_position_router
from handlers.user.get.search_by_project import router as search_by_project_router

router = Router()
router.include_router(get_router)
router.include_router(search_by_name_router)
router.include_router(search_by_date_router)
router.include_router(search_by_position_router)
router.include_router(search_by_project_router)
