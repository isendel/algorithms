"""
Given array of non negative numbers. Need to find start and edn index of subarray that is equal to given number.
Array is 1-indexed
"""

n = int(input())
inputs = [None] * n
input_products = [None] * n
for i in range(n):
    expected = [int(x) for x in input().split()]
    input_products[i] = expected[1]
    inputs[i] = [int(x) for x in input().split()]

for i in range(len(inputs)):
    A = inputs[i]
    p = input_products[i]
    start_idx = 0
    end_idx = 0
    current_sum = A[0]
    if len(A) == 1 and current_sum == p:
        print('1 1')
    elif len(A) > 1:
        while end_idx < len(A) - 1:
            print('[%s, %s] -> %s' % (start_idx, end_idx, current_sum))
            if current_sum == p:
                break
            if current_sum + A[end_idx + 1] <= p:
                print('Current sum is rising. Increase end_idx')
                current_sum += A[end_idx + 1]
                end_idx += 1
            else:
                print('Current sum overflow. Increase start_idx %s -> %s' % (start_idx, start_idx + 1))
                current_sum -= A[start_idx]
                start_idx += 1
    if current_sum != p:
        print(-1)
    else:
        print(start_idx + 1, end_idx + 1)
