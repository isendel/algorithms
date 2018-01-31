def solution(A):
    # kadane's approach for max slice problem

    a_normalized = [0] * len(A)
    for i in range(1, len(A)):
        a_normalized[i] = A[i] - A[i - 1]

    max_ending = max_slice = 0
    for a in a_normalized:
        max_ending = max(a, max_ending + a)
        max_slice = max(max_slice, max_ending)

    return max_slice
