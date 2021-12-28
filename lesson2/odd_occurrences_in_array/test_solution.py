from solution import solution

import pytest


@pytest.mark.parametrize(
    ["A", "res"],
    [
        ([1, 2, 3, 1, 2, 3, 4, 5, 4, ], 5),
        ([1, 1, 2, 2, 3], 3)
    ]
)
def test_solution(A, res):
    assert solution(A) == res