import pytest
from solution import solution

# Check if an array is a permutation
# A permutation is an array that has all values of a sequence from 1 to N
# once and only once

### Constraints ###

N_RANGE = (1, 100000)

VALUES_RANGE = (1, 1000000000)



@pytest.mark.parametrize(
    ['A', "res"],
    [
        ([4, 1, 3, 2], 1),
        ([4, 1, 3], 0),
        ([2], 0),
        ([1], 1),
        ([1, 1], 0),
        ([3, 2, 4, 5], 0),
        ([3, 2, 4, 5, 1], 1),
        ([3, 2, 4, 5, 1, 2], 0),
        ([3, 2, 4, 5, 1, 2, 100], 0)
    ]
)
def test_solution(A, res):
    assert solution(A) == res
