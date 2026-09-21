import pytest

'''
Перепиши этот тест через @pytest.mark.parametrize, чтобы он проверял is_even сразу на нескольких парах "число → ожидаемый результат":

4 → True
7 → False
0 → True

Плюс добавь каждому кейсу осмысленный id (по аналогии с тем, что только что разобрали).
'''
def is_even(n: int) -> bool:
    return n % 2 == 0

@pytest.mark.parametrize(
    "n, expected",
    [
        pytest.param(4, True, id="четное_4"),
        pytest.param(7, False, id="нечетное_7"),
        pytest.param(0, True, id="четное_0"),
    ]
)
def test_is_even(n: int, expected: bool):
    assert is_even(n) is expected
