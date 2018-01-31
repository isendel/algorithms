from collections import deque


def solution(A):
    N = len(A)

    peaks_values = deque()
    peaks = [False] * N
    for i in range(1, N - 1):
        if A[i] > max(A[i - 1], A[i + 1]):
            peaks[i] = True
            peaks_values.append(i)

    peaks_count = len(peaks_values)
    for i in range(peaks_count + 1, 1, -1):
        if check(i, peaks):
            return i

    return 1 if peaks_count == 1 else 0


def check(x, peaks):
    """
    Check if x number of flags can be placed on peaks A
    :param x: number of flags
    :param peaks: peaks location
    :return: True if x number of flags can be placed on peaks
    """
    N = len(peaks)
    flags = x
    pos = 0
    while pos < N and flags > 0:
        # print('Checking peaks at position: %s/%s' % (pos, N))
        if peaks[pos]:
            flags -= 1
            pos += x
        else:
            pos += 1

    return flags == 0
