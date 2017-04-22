from collections import deque

def solution(H):
    levels = deque()
    blocks = 0
    for i in xrange(len(H)):
        print H[i]
        while len(levels) > 0 and levels[-1] > H[i]:
            levels.pop()
            print 'Going down, H: %s, levels: %s' % (H[i], levels)
            blocks += 1
        if len(levels) == 0 or levels[-1] < H[i]:
            levels.append(H[i])
            print 'Going up, H: %s, levels: %s' % (H[i], levels)
    
    return blocks + len(levels)
