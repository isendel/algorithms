def get_prefix_sum(A):
    result = [0] * (len(A) + 1)
    for i in xrange(1, len(A) + 1):
        result[i] = result[i - 1] + A[i -1]
    return result

def solution(S, P, Q):
    hasA = get_prefix_sum([s == 'A' for s in S])
    hasC = get_prefix_sum([s == 'C' for s in S])
    hasG = get_prefix_sum([s == 'G' for s in S])
    hasT = get_prefix_sum([s == 'T' for s in S])
    result = [0] * len(P)
    for i in xrange(len(P)):
        p = P[i]
        q = Q[i]
        if hasA[q+1] - hasA[p] > 0:
            result[i] = 1
        elif hasC[q+1] - hasC[p] > 0:
            result[i] = 2
        elif hasG[q+1] - hasG[p] > 0:
            result[i] = 3
        elif hasT[q+1] - hasT[p] > 0:
            result[i] = 4

    return result
