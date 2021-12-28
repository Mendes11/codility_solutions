def solution(X, A):
    # write your code in Python 3.6
    # We are interested in counting the occurrence of all values until X
    counter = [0] * (X + 1)
    non_repeated_leafs = 0
    for i in range(len(A)):
        counter[A[i]] += 1
        if counter[A[i]] == 1 and A[i] <= X:
            non_repeated_leafs += 1

        if non_repeated_leafs == X:
            return i

    return -1
