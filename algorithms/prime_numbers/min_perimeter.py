def solution(N):
    """
    Compute min perimeter of rectangle who's area is N
    :param N: area of rectangle
    :return: min perimeter of rectangle
    """
    i = 1
    min_perimeter = float('inf')
    while i * i <= N:
        if N % i == 0 or i * i == N:
            min_perimeter = int(min(min_perimeter, 2 * (i + N / i)))
        i += 1

    return min_perimeter
