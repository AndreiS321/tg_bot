import asyncio

from bot import dp, bot
from database.db import Database
from handlers.admin.service import router as service_router
from handlers.admin.common import router as common_router
from handlers.admin.create import router as add_router
from handlers.user.get import router as get_router
from handlers.admin.update import router as update_router
from handlers.admin.delete import router as delete_router


async def register_routers() -> None:
    dp.include_router(service_router)
    dp.include_router(add_router)
    dp.include_router(get_router)
    dp.include_router(update_router)
    dp.include_router(delete_router)
    dp.include_router(common_router)


async def setup_bot():
    bot.db = Database()
    await register_routers()


async def main():
    await setup_bot()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
