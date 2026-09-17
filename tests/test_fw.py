import pytest

@pytest.fixture
def answer():
    return 42

def test_value(answer):
    assert answer == 42
