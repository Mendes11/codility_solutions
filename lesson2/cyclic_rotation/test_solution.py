import pytest

from solution import solution


@pytest.mark.parametrize(
    ["arr", 'K', "res"],
    [
        ([], 0, []),
        ([], 2, []),
        ([1, 2], 1, [2, 1]),
        ([1, 2], 2, [1, 2]),
        ([1, 2], 3, [2, 1]),
        ([1, 2, 3, 4, 5, 6], 4, [3, 4, 5, 6, 1, 2])
    ]
)
def test_solution(arr, K, res):
    assert solution(arr, K) == res