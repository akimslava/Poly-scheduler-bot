from enum import Enum


class Options(Enum):
    SELECT_TODAY = 'SELECT_TODAY',
    SELECT_TOMORROW = 'SELECT_TOMORROW',
    SELECT_WEEK = 'SELECT_WEEK',

    def value_of(self) -> str:
        return self.value[0]
