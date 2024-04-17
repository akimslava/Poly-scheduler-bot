import asyncio
import logging

from aiogram.filters import Command

from src.handlers.basic import get_start
from src.settings import settings
from src.utils.commands import set_commands
from src.utils.kit import bot, dp
from src import messages as msg


async def start_bot():
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_message_id, text=msg.START_BOT)


async def stop_bot():
    await bot.send_message(settings.bots.admin_message_id, text=msg.STOP_BOT)


async def start():
    logging.basicConfig(level=logging.INFO)

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    dp.message.register(get_start, Command(commands='start'))

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())
