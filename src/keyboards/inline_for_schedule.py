from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.keyboards.options import Options
from src.keyboards import messages as msg


def confirm_question() -> InlineKeyboardMarkup:
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.row(
        InlineKeyboardButton(
            text=msg.SELECT_YES,
            callback_data=Options.SUPPORT_SELECT_YES.value_of()
        ),
        InlineKeyboardButton(
            text=msg.SELECT_NO,
            callback_data=Options.SUPPORT_SELECT_NO.value_of()
        )
    )
    return keyboard_builder.as_markup()
