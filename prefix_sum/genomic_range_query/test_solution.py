import pytest
from solution import solution


@pytest.mark.parametrize(
    ['S', 'P', 'Q', 'res'],
    [
        ('CAGCCTA', [2, 5, 0], [4, 5, 6], [2, 4, 1])
    ]
)
def test_solution(S, P, Q, res):
    assert solution(S, P, Q) == res
