from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from src.utils.kit import dp, data_base
from src.handlers import messages as msg
from src.filters.state import WriteGroupNumber
from src.parser.tools import is_groupId_correct, is_int


async def get_start(message: Message, state: FSMContext):
    user_id = message.from_user.id
    first_name = message.from_user.first_name

    if data_base.user_exist(user_id):
        await message.answer(msg.WELCOME_USER.format(first_name))
    else:
        await message.answer(msg.WELCOME_USER.format(first_name) + "\n" + msg.ENTER_GROUP)
        await state.set_state(WriteGroupNumber.writing_group_number)


@dp.message(WriteGroupNumber.writing_group_number)
async def add_new_user_group(message: Message, state: FSMContext):
    if is_int(message.text):
        group_number = int(message.text)

        if is_groupId_correct(group_number):
            user_id = message.from_user.id

            if data_base.add_user(user_id, group_number):
                await message.answer(msg.SUCCESSFULLY_ADDED)

        else:
            await message.answer(msg.INVALID_GROUP_NUMBER)
    else:
        await message.answer(msg.INCORRECT_TYPE)
    await state.clear()
