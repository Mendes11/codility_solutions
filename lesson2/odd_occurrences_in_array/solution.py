def solution(A):
    counts = {}

    for v in A:
        counts[v] = counts.setdefault(v, 0) + 1
    for k, v in counts.items():
        if v % 2 == 1:
            return k
