from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.keyboards.options import Options
from src.keyboards import messages as msg


def choose_day() -> InlineKeyboardMarkup:
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.row(
        InlineKeyboardButton(
            text=msg.TODAY,
            callback_data=Options.SELECT_TODAY.value_of()
        ),
        InlineKeyboardButton(
            text=msg.TOMORROW,
            callback_data=Options.SELECT_TOMORROW.value_of()
        ),
        InlineKeyboardButton(
            text=msg.WEEK,
            callback_data=Options.SELECT_WEEK.value_of()
        ),
    )
    return keyboard_builder.as_markup()
