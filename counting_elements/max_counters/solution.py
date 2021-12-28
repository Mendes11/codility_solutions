def solution(N, A):
    # write your code in Python 3.6
    counter = [0] * N
    base_value = 0
    max_value = 0

    for position in A:
        idx = position - 1

        if position <= N:
            value = max(counter[idx], base_value)
            counter[idx] = value + 1

            if counter[idx] > max_value:
                max_value = counter[idx]
        else:
            base_value = max_value

    # Finish with a final iteration through all data
    # To correct the counter values bellow the base value
    return [max(v, base_value) for v in counter]
