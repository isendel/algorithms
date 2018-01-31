def solution(A):
    if len(A) == 2:
        return abs(A[0] - A[1])

    total_sum = sum(A)
    min_diff = total_sum
    left_sum = 0
    for i in range(len(A) - 1):
        left_sum += A[i]
        right_sum = total_sum - left_sum
        min_diff = min(min_diff, abs(left_sum - right_sum))

    return min_diff