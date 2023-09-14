from aiogram import Bot as AiogramBot
from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from config import BotConfig
from database.db import Database

storage = MemoryStorage()


class Bot(AiogramBot):
    db: Database


bot = Bot(token=BotConfig.token, parse_mode="HTML")
dp = Dispatcher(storage=storage)
