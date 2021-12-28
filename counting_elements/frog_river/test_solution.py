from solution import solution
import pytest

## Constraints ##

N_SIZE = [1, 100000]
X_RANGE = [1, 100000]


@pytest.mark.parametrize(
    ["A", "X", "res"],
    [
        ([1, 3, 1, 4, 2, 3, 5, 4], 5, 6),
        ([1], 1, 0),
        ([1, 1], 1, 0),
        ([2, 1], 2, 1),
        ([3, 1, 1, 1, 2, 1, 3], 3, 4),
        ([3], 5, -1),
    ]
)
def test_solution(A, X, res):
    assert solution(X, A) == res
