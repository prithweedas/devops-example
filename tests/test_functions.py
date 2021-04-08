# tests/test_functions.py

from app.functions import add
def test_add():
    assert add(1, 1) == 2
    assert add(1, 2) == 3