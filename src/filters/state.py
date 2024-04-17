from aiogram.fsm.state import StatesGroup, State


class WriteGroupNumber(StatesGroup):
    writing_group_number = State()
