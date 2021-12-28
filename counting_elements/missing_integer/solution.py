def solution(A):
    # Need to count all values from this range
    # And return the first positive value that does not occur

    next_integer = 1  # Expected Minimal Positive Integer

    # Sort the array to iterate the sequence
    for value in sorted(A):
        if value == next_integer:
            next_integer += 1

    return next_integer
