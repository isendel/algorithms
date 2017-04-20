#Each element at position i in array A is radius of disc at position i. We need to find number of intersections between all discsc.
def solution(A):
    range_lower = sorted([i - A[i] for i in xrange(len(A))])
    range_upper = sorted([i + A[i] for i in xrange(len(A))])
    print range_lower
    print range_upper
    intersections = 0
    open_discs = 0
    l_idx = 0
    u_idx = 0
    while l_idx != len(A) and u_idx != len(A):
        if range_lower[l_idx] <= range_upper[u_idx]:
            intersections += open_discs
            open_discs += 1
            print 'l: %s. Disc opened at %s. Current open discs count: %s, int: %s' % (l_idx, range_lower[l_idx], open_discs, intersections)
            l_idx += 1
        else:
            open_discs -= 1
            print 'u: %s. Disc closed at %s. Current open discs count: %s, int: %s' % (u_idx, range_upper[u_idx], open_discs, intersections)
            u_idx += 1
        if intersections > 10000000:
            return -1
    
    return intersections
