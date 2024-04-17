from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from src.utils.kit import dp, data_base
from src.handlers import messages as msg
from src.filters.state import WriteGroupNumber


async def get_start(message: Message, state: FSMContext):
    user_id = message.from_user.id
    first_name = message.from_user.first_name

    if data_base.user_exist(user_id):
        await message.answer(msg.WELCOME_USER.format(first_name))
    else:
        await message.answer(msg.WELCOME_USER.format(first_name))
        await state.set_state(WriteGroupNumber.writing_group_number)


@dp.message(WriteGroupNumber.writing_group_number)
async def add_new_user_group(message: Message, state: FSMContext):
    group_number = int(message.text)
    user_id = message.from_user.id
    data_base.add_user(user_id, group_number)
    await message.answer("Kek")
    await state.clear()

