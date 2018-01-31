# Fishes are in array A. A[i] is how fish i is big
# B array represent direction: 0 - upstream, 1 downstream
# If fish flowing upstream meets downstream fish - larger one eats smaller.
# Count number of live fishes.
from collections import deque


def solution(A, B):
    up = deque()
    down = deque()

    for i in range(len(A)):
        curr_fish_alive = True
        curr_fish = A[i]
        # if fish going upstream
        if B[i] == 0:
            while curr_fish_alive and len(down) > 0 and down[-1] != curr_fish:
                if down[-1] > curr_fish:
                    curr_fish_alive = False
                elif down[-1] < curr_fish:
                    down.pop()
            if curr_fish_alive:
                up.append(curr_fish)
        else:
            down.append(curr_fish)

    return len(up) + len(down)
