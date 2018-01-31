# Find index of element that occurs more then len(A)//n times in array A
from collections import deque


def solution(A):
    size = 0
    value = None
    last_idx = deque()
    for i, a in enumerate(A):
        if size == 0:
            value = a
            size += 1
            last_idx.append(i)
        else:
            if value != a:
                size -= 1
                last_idx.pop()
            else:
                value = a
                size += 1
                last_idx.append(i)

    candidate_count = 0
    if value is not None:
        for a in A:
            if a == value:
                candidate_count += 1

    # print(value, candidate_count, len(A) // 2, last_idx)
    return last_idx[-1] if candidate_count > len(A) // 2 else -1
