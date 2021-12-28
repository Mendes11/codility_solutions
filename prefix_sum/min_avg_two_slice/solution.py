from itertools import zip_longest


def solution(A):
    """
    A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P < Q < N, is called a slice of array A (notice that the slice contains at least two elements). The average of a slice (P, Q) is the sum of A[P] + A[P + 1] + ... + A[Q] divided by the length of the slice. To be precise, the average equals (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1).

    For example, array A such that:

        A[0] = 4
        A[1] = 2
        A[2] = 2
        A[3] = 5
        A[4] = 1
        A[5] = 5
        A[6] = 8
    contains the following example slices:

    slice (1, 2), whose average is (2 + 2) / 2 = 2;
    slice (3, 4), whose average is (5 + 1) / 2 = 3;
    slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.
    The goal is to find the starting position of a slice whose average is minimal.

    Write a function:

    def solution(A)

    that, given a non-empty array A consisting of N integers, returns the starting position of the slice with the minimal average. If there is more than one slice with a minimal average, you should return the smallest starting position of such a slice.

    For example, given array A such that:

        A[0] = 4
        A[1] = 2
        A[2] = 2
        A[3] = 5
        A[4] = 1
        A[5] = 5
        A[6] = 8
    the function should return 1, as explained above.

    Write an efficient algorithm for the following assumptions:

    N is an integer within the range [2..100,000];
    each element of array A is an integer within the range [−10,000..10,000].
    """

    # So, the trick here is that you only need the averages of 2 or 3 steps
    # ahead. Any more than this will not be minimal, because it will contain
    # the minimal average inside it!
    P1 = (prefix_sum_n_mean(A, 2))
    P2 = (prefix_sum_n_mean(A, 3))

    if not P2:
        return 0 # P2 empty means we only have two values

    starting_point = -1
    min_avg = 100001

    for i, (avg_2, avg_3) in enumerate(zip_longest(P1, P2)):
        if avg_2 < min_avg:
            min_avg = avg_2
            starting_point = i
        if avg_3 is not None and avg_3 < min_avg:
            min_avg = avg_3
            starting_point = i

    return starting_point


def prefix_sum_n_mean(A, n_values):
    """
    Calculates the average of the n_values ahead of each position of list A

    :param A: list
    :param n_means: number of values to use for each average
    :return: list of averages
    """
    n = len(A) - (n_values - 1)
    P = [10000] * n
    for k in range(n):
        P[k] = 0
        for i in range(n_values):
            P[k] += A[k + i]
        P[k] /= n_values

    return P
