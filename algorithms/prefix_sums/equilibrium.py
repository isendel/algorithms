def get_prefix_sum(A):
    pref = [0] * (len(A) + 1)
    for i in range(1, len(A) + 1):
        pref[i] = pref[i - 1] + A[i - 1]
    return pref


n = int(input())
inputs = [None] * n
for i in range(n):
    expected = [int(x) for x in input().split()]
    inputs[i] = [int(x) for x in input().split()]

for i in range(len(inputs)):
    A = inputs[i]
    N = len(A)
    pref_left = get_prefix_sum(A)
    pref_right = get_prefix_sum(A[::-1])[::-1]

    result = -1
    for i in range(len(A)):
        if pref_left[i] - pref_right[i + 1] == 0:
            result = i + 1
            break
    print(result)
