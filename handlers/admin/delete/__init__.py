from aiogram import Router

from handlers.admin.delete.delete import router as delete_router
from handlers.middlewares import AdminOnly

router = Router()
router.include_router(delete_router)
router.message.middleware(AdminOnly())
