import pytest
from solution import solution

## Constraints ##
N_RANGE = (1, 100000)
M_RANGE = (1, 100000)


@pytest.mark.parametrize(
    ["N", "A", "res"],
    [
        (5, [3, 4, 4, 6, 1, 4, 4], [3, 2, 2, 4, 2]),
        (1, [1, 1, 1], [3]),
        (1, [2, 1, 1], [2]),
        (1, [2], [0]),
        (1, [1, 1, 2, 2], [2]),
        (2, [1, 1, 2, 1], [3, 1]),
        (3, [1, 1, 4, 2, 1, 4, 3, 2, 4], [4, 4, 4]),
        # Worst Case
        (N_RANGE[1], [N_RANGE[1] + 1] * M_RANGE[1], [0] * N_RANGE[1])
    ]
)
def test_solution(N, A, res):
    assert solution(N, A) == res
