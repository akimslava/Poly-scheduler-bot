from enum import Enum


class Options(Enum):
    SELECT_YES = 'SELECT_YES',
    SELECT_NO = 'SELECT_NO',

    def value_of(self) -> str:
        return self.value[0]
