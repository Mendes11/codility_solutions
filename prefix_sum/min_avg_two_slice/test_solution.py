import pytest
from solution import solution


@pytest.mark.parametrize(
    ['A', 'res'],
    [
        ([4, 2, 2, 5, 1, 5, 8], 1),
        ([10000, -10000], 0),
        ([5, 6, 3, 4, 9], 2),
        ([-3, -5, -8, -4, -10], 2),
    ]
)
def test_solution(A, res):
    assert solution(A) == res

