n = int(input())
inputs1 = [None] * n
inputs2 = [None] * n
for i in range(n):
    expected = [x for x in input().split()]
    inputs1[i] = [x for x in input().split()]
    inputs2[i] = [x for x in input().split()]

for i in range(len(inputs1)):
    X = inputs1[i][0]
    Y = inputs2[i][0]
    m = len(X)
    n = len(Y)

    L = [[None] * (n + 1) for i in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
    print(L[m][n])
