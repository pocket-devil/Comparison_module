import pytest

#фу-ция возведения в квадрат
def square(n: int) -> int:
    return n * n



#параметры для теста "Возведения в квадрат"
@pytest.mark.parametrize(
    ('input_x', 'expected'),
    (
            (1, 1),
            (-1, 1),
            (2, 4),
            (-2, 4),
            (3, 0)
    ),
)


#проверим, какие из заданных значений удовлетворят условия
def test_square(input_x, expected):
    assert square(input_x) == expected
