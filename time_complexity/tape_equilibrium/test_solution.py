import pytest

from solution import solution

@pytest.mark.parametrize(
    ["A", "res"],
    [
        ([3, 1, 2, 4, 3], 1),
        ([1, 3, 5, 3, 10, 4, 20], 2),
        ([20, 10, 3, 5, 3, 10, 4, 2], 3),
        ([-1000, 1000], 2000),
        ([-10, -20, -30, -40, 100], 20)
    ]
)
def test_solution(A, res):
    assert solution(A) == res
