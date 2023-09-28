from aiogram import Router

from handlers.admin.update.update import router as update_router
from handlers.middlewares import AdminOnly

router = Router()
router.include_router(update_router)
router.message.middleware(AdminOnly())
