def count_divisors(n):
    i = 1
    result = 0
    while i * i < n:
        print(n, i, n % i)
        if n % i == 0:
            result += 2
        if i * i == n:
            result += 1
        i += 1
    return result
