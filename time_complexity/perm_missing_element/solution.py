def solution(A):
    size = len(A)
    expectedSum = ((size + 1) * (size + 2)) // 2
    return expectedSum - sum(A)
