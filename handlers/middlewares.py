from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Message

from database.crud.admin import AdminAccessor
from handlers.decorators import get_accessor


class AdminOnly(BaseMiddleware):
    @get_accessor(AdminAccessor)
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
        accessor: AdminAccessor,
    ) -> Any:
        if await accessor.get(tg_id=event.from_user.id):
            return await handler(event, data)
        await event.answer("Нет прав доступа")
