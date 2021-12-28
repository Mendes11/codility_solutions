import pytest
from solution import solution

## Constraints ##
B_RANGE = A_RANGE = [0, int(2e9)]
K_RANGE = [1, int(2e9)]
# A <= B

@pytest.mark.parametrize(
    ["A", "B", "K", "res"],
    [
        (6, 11, 2, 3),
        (6, 6, 4, 0),
        (6, 6, 2, 1),
        (0, 14, 2, 8),
        (0, B_RANGE[-1], 1, B_RANGE[-1] + 1), # Worst case. all are divisible,
    ]
)
def test_solution(A, B, K, res):
    assert solution(A, B, K) == res
