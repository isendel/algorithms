n = int(input())
inputs = [None] * n
input_products = [None] * n
for i in range(n):
    expected = [int(x) for x in input().split()]
    input_products[i] = expected[1]
    inputs[i] = [int(x) for x in input().split()]

for i in inputs:
    a = inputs[i]
    p = input_products[i]
