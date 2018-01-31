# Fishes are in array A. A[i] is how fish i is big
# B array represent direction: 0 - upstream, 1 downstream
# If fish flowing upstream meets downstream fish - larger one eats smaller.
# Count number of live fishes.
from collections import deque
def solution(A, B):
    up = deque()
    down = deque()
    for i in xrange(len(A)):
        if B[i] == 0:
            up.append(A[i])
            print 'Fish %s:%s is flowing upstream.' % (i, A[i])
            while len(down) > 0 and A[i] > down[-1]:
                print 'Fish %s:%s eat %s' % (i, A[i], down[-1])
                down.pop()
            if len(down) > 0 and A[i] < down[-1]:
                print 'Fish %s:%s eat %s' % (i, down[-1], A[i])
                up.pop()
        else:
            down.append(A[i])
            print 'Fish %s:%s is flowing downstream.' % (i, A[i])
    return len(up) + len(down)
    
