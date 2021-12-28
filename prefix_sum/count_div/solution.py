# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def _num_dividends(P, K):
    """
    Returns the number of multiples of K for a 0 index sequence P.
    :param P:
    :param K:
    :return:
    """
    return (P // K) + 1


def solution(A, B, K):
    """
    Given Integers A, B and K

    Return the number of integers within range [A, B] that are divisible by K

    {i: A <= i <= B, i mod K = 0}

    :param A:
    :param B:
    :param K:
    :return:
    """

    # For 1 <= K < 2e9
    # There are K possible values m = x % K, starting at 0
    # Such as 0 <= m < K

    # At position B, there are a total of ((B / K) + 1) dividends
    total_b_dividends = _num_dividends(B, K)
    total_a_dividends = _num_dividends(A - 1, K)

    return total_b_dividends - total_a_dividends

