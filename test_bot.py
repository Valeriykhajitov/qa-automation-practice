
import pytest
from bot import save_to_memory

@pytest.mark.parametrize("input_text, expected", [
    ("здоров будь", "saved"),
    ("ахахахаха", "skipped"),
    ("hahahaha", "skipped"),
    ("лол", "skipped"),
    ("кек", "skipped"),
    ("ору", "skipped"),
    ("привет мир", "saved"),
    ("ааааааааааа", "skipped"),
    ("хахахахахахаха", "skipped"),
    ("lmao", "skipped"),
    ("xd", "skipped"),
])

def test_save_to_memory(input_text, expected):
    assert save_to_memory(input_text) == expected