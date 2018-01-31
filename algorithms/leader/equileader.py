def solution(A):
    value = None
    size = 0
    for i, a in enumerate(A):
        if size == 0:
            value = a
            size += 1
        else:
            if value != a:
                size -= 1
            else:
                value = a
                size += 1

    candidate_count = 0
    for a in A:
        if a == value:
            candidate_count += 1

    # is leader found
    if candidate_count > len(A)//2:
        #print('Leader found: %s occured %s ' % (value, candidate_count))
        curr_leader_count = 0
        result_count = 0
        for i in range(len(A) - 1):
            a = A[i]
            if a == value:
                curr_leader_count += 1
            #print('Compare %s/%s -> %s/%s' % (curr_leader_count, i + 1, candidate_count - curr_leader_count,len(A) - i - 1))
            if curr_leader_count > (i + 1) // 2 and (candidate_count - curr_leader_count) > (len(A) - i - 1) // 2:
                result_count += 1

        return result_count

    return 0