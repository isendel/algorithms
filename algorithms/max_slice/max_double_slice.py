def solution(A):
    print(A)
    if len(A) == 3:
        return 0

    if len(A) == 4:
        return max(A[1], A[2])

    max_ending_f = 0
    max_ending_b = 0

    # initial max double sum

    ms_f = [0] * len(A)
    ms_b = [0] * len(A)

    mds = -float('inf')

    for i in range(1, len(A) - 1):
        max_ending_f = max(A[i], max_ending_f + A[i])
        max_ending_b = max(A[-(i + 1)], max_ending_b + A[-(i + 1)])

        ms_f[i] = max_ending_f
        ms_b[-(i + 1)] = max_ending_b
    print(ms_f)
    print(ms_b)

    for i in range(1, len(A) - 1):
        current_mds = max(ms_f[i - 1] + ms_b[i + 1], ms_f[i - 1], ms_b[i + 1])
        mds = max(mds, current_mds)

    return mds
