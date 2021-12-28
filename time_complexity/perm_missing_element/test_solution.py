import pytest

from solution import solution

@pytest.mark.parametrize(
    ["A", "res"],
    [
        ([2, 1, 4, 5, 6, 7, 9, 8], 3),
        ([1, 2, 4, 5, 3, 9, 8, 7], 6)
    ]
)
def test_solution(A, res):
    assert solution(A) == res
