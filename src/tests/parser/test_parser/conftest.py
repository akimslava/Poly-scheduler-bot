import pytest

from unittest.mock import MagicMock


@pytest.fixture
def mock_data():
    return {
        'time_start': '09:00',
        'time_end': '10:30',
        'subject': 'Mathematics',
        'typeObj': {'name': 'Lecture'},
        'teachers': [{'full_name': 'John Doe'}],
        'auditories': [{'name': '101', 'building': {'name': 'Main Building'}}]
    }


@pytest.fixture
def mock_day_data(mock_data):
    return {'lessons': [mock_data]}


@pytest.fixture
def mock_get_data():
    mock_schedule = {
        'days': [{'weekday': 1, 'date': '2024-05-06', 'lessons': []}]
    }
    return MagicMock(return_value=mock_schedule)
