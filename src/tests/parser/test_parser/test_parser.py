import pytest
from unittest.mock import patch

from src.parser.parser import parse_subject, parse_day, get


@pytest.mark.asyncio
async def test_parse_subject(mock_data):
    result = await parse_subject(mock_data)
    assert result == """09:00 - 10:30 Mathematics
              Lecture
              John Doe
              101, Main Building\n"""


@pytest.mark.asyncio
async def test_parse_day(mock_day_data):
    result = await parse_day(mock_day_data)
    assert result == """09:00 - 10:30 Mathematics
              Lecture
              John Doe
              101, Main Building\n\n"""


@pytest.mark.asyncio
async def test_get(mock_get_data):
    with patch("src.parser.tools.getData", mock_get_data):
        result = await get("на неделю", 38734)
    assert "Понедельник (2024-05-06)" in result
