# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

N_RANGE = (1, 100000)

# We should not use a counter with this values due to the huge values range
VALUES_RANGE = (1, 1000000000)


def solution(A):
    # write your code in Python 3.6
    # we create a counter of just the possible values
    size = len(A)
    counter = [0] * size
    unique_counts = 0

    for i in range(len(A)):
        try:
            counter[A[i] - 1] += 1
            unique_counts += 1
        except IndexError:
            return 0

        if counter[A[i] - 1] > 1:
            return 0

    if unique_counts == size:
        return 1

    return 0
