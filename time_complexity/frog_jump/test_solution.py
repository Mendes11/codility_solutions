from solution import solution
import pytest

@pytest.mark.parametrize(
    ["x", "y", "d", 'res'],
    [
        (10, 85, 30, 3),
        (10, 100, 30, 3),
        (10, 115, 30, 4),
        (10, 100, 10, 9),
        (5, 105, 3, 34)
    ]
)
def test_solution(x, y, d, res):
    assert solution(x, y, d) == res
