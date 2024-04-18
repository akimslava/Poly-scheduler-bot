from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

import src.keyboards.inline_for_schedule as kb
from src.parser.parser import get
from src.filters.state import UpdateGroupNumber
from src.utils.kit import dp, bot, data_base
from src.handlers import messages as msg
from src.keyboards.options import Options
from src.parser.tools import is_groupId_correct, is_int


async def get_schedule(message: Message):
    await message.answer(msg.SELECT_DAY, reply_markup=kb.choose_day())


async def update_group_number(message: Message, state: FSMContext):
    await message.answer(msg.ENTER_GROUP)
    await state.set_state(UpdateGroupNumber.writing_group_number)


@dp.message(UpdateGroupNumber.writing_group_number)
async def set_new_group_number(message: Message, state: FSMContext):
    if is_int(message.text):
        group_number = int(message.text)

        if is_groupId_correct(group_number):
            user_id = message.from_user.id

            if data_base.update_group_number(user_id, group_number):
                await message.answer(msg.SUCCESSFULLY_MODIFIED)

        else:
            await message.answer(msg.INVALID_GROUP_NUMBER)
    else:
        await message.answer(msg.INCORRECT_TYPE)
    await state.clear()


@dp.callback_query(F.data == Options.SELECT_TODAY.value_of())
async def select_today(call: CallbackQuery):
    group_id = data_base.get_group_id(call.message.chat.id)
    try:
        message = await get(msg.TODAY, group_id)
        await bot.edit_message_text(
            text=message,
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            reply_markup=None
        )
    finally:
        await call.answer()


@dp.callback_query(F.data == Options.SELECT_TOMORROW.value_of())
async def select_tomorrow(call: CallbackQuery):
    group_id = data_base.get_group_id(call.message.chat.id)
    try:
        message = await get(msg.TOMORROW, group_id)
        await bot.edit_message_text(
            text=message,
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            reply_markup=None
        )
    finally:
        await call.answer()


@dp.callback_query(F.data == Options.SELECT_WEEK.value_of())
async def select_week(call: CallbackQuery):
    group_id = data_base.get_group_id(call.message.chat.id)
    try:
        message = await get(msg.WEEK, group_id)
        await bot.edit_message_text(
            text=message,
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            reply_markup=None
        )
    finally:
        await call.answer()
