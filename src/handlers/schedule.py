from aiogram.types import Message
from aiogram.fsm.context import FSMContext

import src.keyboards.inline_for_schedule as kb
from src.utils.kit import dp, data_base
from src.handlers import messages as msg
from src.filters.state import WriteGroupNumber


async def get_schedule(message: Message, state: FSMContext):
    await message.answer("Выберите на какой день хотите расписание", reply_markup=kb.confirm_question())


@dp.message(WriteGroupNumber.writing_group_number)
async def add_new_user_group(message: Message, state: FSMContext):
    group_number = int(message.text)
    user_id = message.from_user.id
    data_base.add_user(user_id, group_number)
    await state.clear()