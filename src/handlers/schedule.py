import asyncio
from aiogram import F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

import src.keyboards.inline_for_schedule as kb
from src.parser.parser import get
from src.utils.kit import dp, bot, data_base
from src.handlers import messages as msg
from src.keyboards.options import Options


async def get_schedule(message: Message, state: FSMContext):
    await message.answer("Выберите на какой день хотите расписание", reply_markup=kb.choose_day())


@dp.callback_query(F.data == Options.SELECT_TODAY.value_of())
async def select_yes(call: CallbackQuery):
    group_id = data_base.get_group_id(call.message.chat.id)
    try:
        message = await get("на сегодня", group_id)
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
        message = await get("на завтра", group_id)
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
        message = await get("на неделю", group_id)
        await bot.edit_message_text(
            text=message,
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            reply_markup=None
        )
    finally:
        await call.answer()
