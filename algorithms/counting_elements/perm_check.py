def solution(A):
    if len(A) == 1:
        return 1 if A[0] == 1 else 0

    min_a = 1
    n = len(A)
    max_a = n

    expected_sum = int(n * (min_a + max_a)/2)
    actual_sum = sum(set(A))

    print('expected: %s, got: %s' % (expected_sum, actual_sum))

    return 1 if expected_sum == actual_sum else 0