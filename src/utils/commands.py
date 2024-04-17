from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command='start', description='Поздороваться с ботом'),
        BotCommand(command='schedule', description='Получить расписание'),
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())
