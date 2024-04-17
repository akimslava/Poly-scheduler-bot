from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from src.settings import settings

bot = Bot(token=settings.bots.bot_token, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot=bot)
