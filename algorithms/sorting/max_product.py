import itertools as it


def solution(A):
    """
    :param A: input array of numbers
    :return: max product of any 3 numbers from array A
    """
    A = sorted(A)
    max_product = -float('inf')
    for a in it.combinations(A[:3] + A[-3:] if len(A) > 6 else A, 3):
        curr_product = a[0] * a[1] * a[2]
        # print(a, curr_product)
        max_product = max(max_product, curr_product)

    return max_product
