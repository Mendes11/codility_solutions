# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
N_RANGE = (1, 100000)
M_RANGE = [1, 50000]


def solution(S, P, Q):
    """
    We cum sum all impacts for each nucleotide at each position

    then, for each query, we simply subtract the sum of the end minus the
    sum until the start and start to check if this subtraction is higher
    than 0.

    If it is, then it means that that nucleotide exists within the query range
    and therefore, if we assert starting from A until T, we can therefore
    return the minimal impact value.
    """
    m = len(P)
    n = len(S)
    res = [0] * m

    # Mount the prefix sum of each nucleotide in the sequence
    a_prefix_sum = [0] * (n + 1)
    c_prefix_sum = [0] * (n + 1)
    g_prefix_sum = [0] * (n + 1)
    t_prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        a_prefix_sum[i] = a_prefix_sum[i - 1]
        c_prefix_sum[i] = c_prefix_sum[i - 1]
        g_prefix_sum[i] = g_prefix_sum[i - 1]
        t_prefix_sum[i] = t_prefix_sum[i - 1]

        if S[i - 1] == 'A':
            a_prefix_sum[i] += 1
        elif S[i - 1] == 'C':
            c_prefix_sum[i] += 2
        elif S[i - 1] == 'G':
            g_prefix_sum[i] += 3
        elif S[i - 1] == 'T':
            t_prefix_sum[i] += 4

    # Now, perform the queries
    for i in range(m):
        start = P[i]
        stop = Q[i]

        if a_prefix_sum[stop + 1] - a_prefix_sum[start] > 0:
            res[i] = 1
        elif c_prefix_sum[stop + 1] - c_prefix_sum[start] > 0:
            res[i] = 2
        elif g_prefix_sum[stop + 1] - g_prefix_sum[start] > 0:
            res[i] = 3
        else:
            res[i] = 4

    return res
