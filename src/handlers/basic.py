from aiogram.types import Message

from src.handlers import messages as msg


async def get_start(message: Message):
    first_name = message.from_user.first_name
    await message.answer(msg.WELCOME_USER.format(first_name))
