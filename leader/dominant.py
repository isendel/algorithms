# Find index of element that occurs more then len(A)//n times in array A
def solution(A):
    n = len(A)
    size = 0
    for k in xrange(n):
        if size == 0:
            size += 1
            value = A[k]
        else:
            if value != A[k]:
                size -= 1
            else:
                size += 1
    result = -1
    count = 0
    if size > 0:
        candidate = value
        for i in xrange(n):
            if A[i] == candidate:
                count += 1
                result = i
    return result if count > n//2 else -1
