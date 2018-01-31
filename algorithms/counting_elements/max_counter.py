def solution(N, A):
    counters = [0] * N
    max_val = 0
    pre_max_val = 0
    for a in A:
        if a <= N:
            if counters[a - 1] < pre_max_val:
                counters[a - 1] = pre_max_val
            counters[a - 1] += 1
            curr_val = counters[a - 1]
            max_val = max(max_val, curr_val)
        else:
            pre_max_val = max_val

    for i in range(N):
        if counters[i] < pre_max_val:
            counters[i] = pre_max_val

    return counters
