from aiogram import Router

from handlers.admin.create.create import router as create_router
from handlers.middlewares import AdminOnly

router = Router()
router.include_router(create_router)
router.message.middleware(AdminOnly())
