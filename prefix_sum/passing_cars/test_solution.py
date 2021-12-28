import pytest
from solution import solution

## Constraints ##
N_RANGE = (1, 100000)

@pytest.mark.parametrize(
    ["A", "res"],
    [
        ([0, 1, 0, 1, 1], 5),
        ([0], 0),
        ([1], 0),
        ([1, 1], 0),
        ([0, 0], 0),
        ([0, 1], 1),
        ([1, 0], 0),
        ([0] * N_RANGE[1], 0),
        (([0] * (N_RANGE[1] // 2)) + ([1] * (N_RANGE[1] // 2)), -1)
    ]
)
def test_solution(A, res):
    assert solution(A) == res
