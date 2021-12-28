## Constraints ##

SIZE = (2, 100000)
VALUE_RANGE = (-1000, 1000)
# 0 < P < N


def _worst_complexity(A):
    size = len(A)
    minimal = 2000

    for i in range(1, size):
        abs_diff = abs(sum(A[:i]) - sum(A[i:]))
        if abs_diff < minimal:
            minimal = abs_diff

    return minimal

# ([-10, -20, -30, -40, 100], 20)

def _better_solution(A):
    P = 0 # Even though P > 0, here it needs to be equal due to the index starting at 0

    left = A[P] # Minimal size is a single value in left
    right = sum(A[1:]) # And all remaining in the right
    minimal_diff = abs(left - right)
    for P in range(1, len(A) -1):
        # Each time we move to the right, the left side accumulates a new value
        # And the right side subtracts that same value
        left += A[P]
        right -= A[P]
        diff = abs(left - right)
        if diff < minimal_diff:
            minimal_diff = diff

    return minimal_diff

def solution(A):
    return _better_solution(A)
