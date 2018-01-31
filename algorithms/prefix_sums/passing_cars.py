def solution(A):
    p = prefix_sum(A)
    total_count = 0
    for i, a in enumerate(A):
        if a == 0:
            total_count += p[-1] - p[i]
        if total_count > 1000000000:
            return -1

    return total_count


def prefix_sum(A):
    n = len(A)
    p = [0] * (n + 1)
    for k in range(1, n + 1):
        p[k] = p[k - 1] + A[k - 1]

    return p
