import asyncio
import logging

from aiogram.filters import Command
from src.handlers.basic import get_start
from src.handlers.schedule import get_schedule
from src.settings import settings
from src.utils.commands import set_commands
from src.utils.kit import bot, dp, data_base

START_BOT = 'Бот запущен!'
STOP_BOT = 'Бот остановлен!'


async def start_bot():
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_message_id, text=START_BOT)


async def stop_bot():
    data_base.conn.close()
    await bot.send_message(settings.bots.admin_message_id, text=STOP_BOT)


async def start():
    logging.basicConfig(level=logging.INFO)

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    dp.message.register(get_start, Command(commands='start'))
    dp.message.register(get_schedule, Command(commands='schedule'))

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())
