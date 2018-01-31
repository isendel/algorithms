n = int(input())
inputs = [None] * n
for i in range(n):
    expected = [int(x) for x in input().split()]
    inputs[i] = [int(x) for x in input().split()]

for i in range(len(inputs)):
    A = inputs[i]
    N = len(A)
    if N == 1:
        print(1)
    elif N == 0:
        print(0)
    else:
        lis = [1] * N
        i = 1
        while i < N:
            for j in range(0, i):
                if A[j] < A[i] and lis[j] + 1 > lis[i]:
                    lis[i] = lis[j] + 1
            i += 1
        print(max(lis))
