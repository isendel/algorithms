def solution(X, A):
    path = [None] * (X + 1)
    leaves_cnt = 0
    for i, a in enumerate(A):
        if path[a] is None:
            path[a] = i
            leaves_cnt += 1
        if leaves_cnt == X:
            return i

    return -1
