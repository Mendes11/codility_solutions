import pytest

from solution import solution

## Constraints ##

N_RANGE = (1, 100000)
VALUE_RANGE = (-1000000, 1000000)


@pytest.mark.parametrize(
    ["A", "res"],
    [
        ([1, 3, 6, 4, 1, 2], 5),
        ([1, 2, 3], 4),
        ([-1, -3], 1),
        ([1], 2),
        ([1, 1], 2),
        ([2, 1], 3),
        ([2, 2], 1),
        ([VALUE_RANGE[0]] * N_RANGE[1], 1),
        ([VALUE_RANGE[1]] * N_RANGE[1], 1)
    ]
)
def test_solution(A, res):
    assert solution(A) == res
