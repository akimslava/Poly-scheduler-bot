import pytest

from src.parser import tools as tl


@pytest.mark.parametrize(
    "text, expected_output",
    [
        ("123", True),
        ("-312", True),
        ("0", True),
        ("Hi", False),
        ("123 h", False),
        ("", False),
    ]
)
def test_is_int(text, expected_output):
    assert tl.is_int(text) == expected_output


@pytest.mark.parametrize(
    "group_id, expected_output",
    [
        (38734, True),
        (111, False),
        (-111, False),
        (0, False),
    ]
)
def test_is_group_id_correct(group_id, expected_output):
    assert tl.is_groupId_correct(group_id) == expected_output
