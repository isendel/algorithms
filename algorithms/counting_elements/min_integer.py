def solution(A):
    n = len(A)
    sm = [None] * (n + 2)
    for a in A:
        if n >= a > 0:
            sm[a] = a
    for i in range(1, len(sm)):
        if sm[i] is None:
            return i

    return 1
