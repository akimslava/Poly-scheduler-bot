from aiogram import F
from aiogram.types import Message, CallbackQuery

import src.keyboards.inline_for_schedule as kb
from src.parser.parser import get
from src.utils.kit import dp, bot, data_base
from src.handlers import messages as msg
from src.keyboards.options import Options


async def get_schedule(message: Message):
    await message.answer(msg.SELECT_DAY, reply_markup=kb.choose_day())


@dp.callback_query(F.data == Options.SELECT_TODAY.value_of())
async def select_yes(call: CallbackQuery):
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
async def select_yes(call: CallbackQuery):
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
async def select_yes(call: CallbackQuery):
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
