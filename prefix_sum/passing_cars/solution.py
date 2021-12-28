## Constraints ##
N_RANGE = (1, 100000)


def solution(A):
    # 0 = car traveling east
    # 1 = car traveling west
    # Pair of cars (P, Q), where 0 <= P < Q < N
    # When P is traveling to east and Q to west
    n = len(A)
    passing_cars = [0] * (n + 1)
    east_cars = 0

    for i in range(1, n + 1):
        if A[i-1] == 0:
            east_cars += 1
            passing_cars[i] = passing_cars[i - 1]
        else:
            passing_cars[i] = passing_cars[i - 1] + east_cars

        if passing_cars[i] > 1e9:
            return -1

    return passing_cars[-1]
