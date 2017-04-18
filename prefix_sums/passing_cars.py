def prefix_sums(A):
    result = [0] * (len(A) + 1)
    for i in xrange(1, len(A) + 1):
        result[i] = result[i - 1] + A[i - 1]
    return result

def solution(A):
    pref = prefix_sums(A)
    result = 0
    for idx, a in enumerate(A):
        #is car traveling east?
        if a == 0:
            result += pref[len(pref) - 1] - pref[idx + 1]
        if result > 1000000000:
            return -1
    return result

print([0,1,0,1,1])
