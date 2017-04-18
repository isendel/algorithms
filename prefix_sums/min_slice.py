# It is required to find the position of a slice with min avg in the 
# numerical sequence. There is a mathematical proof for such problem
# where only slices of 2 and 3 elements are taken into account.
# Having that, solution become really simple. 
def get_prefix_sum(A):
    result = [0] * (len(A) + 1)
    for i in xrange(1, len(A) + 1):
        result[i] = result[i - 1] + A[i - 1]
    return result

def solution(A):
    pref = get_prefix_sum(A)
    min_i = 0
    min_slice = float(A[0] + A[1])/2.0
    for i in xrange(len(A)):
        if i < len(A) - 2:
            slice_3_avg = float(pref[i + 3] - pref[i])/3.0
            if slice_3_avg < min_slice:
                min_slice = slice_3_avg
                min_i = i
        if i< len(A) - 1:
            slice_2_avg = float(pref[i + 2] - pref[i])/2.0
            if slice_2_avg < min_slice:
                min_slice = slice_2_avg
                min_i = i
    return min_i
