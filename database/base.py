from sqlalchemy.ext.asyncio import AsyncSession

from bot import bot


class BaseAccessor:
    def __init__(self):
        self.session: AsyncSession = bot.db.session_maker()
