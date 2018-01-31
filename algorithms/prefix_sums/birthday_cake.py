#!/bin/python

import sys


# Lily has a chocolate bar consisting of a row of  squares where each square has an integer written on it. She wants to share it with Ron for his birthday, which falls on month  and day . Lily only wants to give Ron a piece of chocolate if it contains  consecutive squares whose integers sum to .
# Given , , and the sequence of integers written on each square of Lily's chocolate bar, how many different ways can Lily break off a piece of chocolate to give to Ron?

def get_prefix_sums(A):
    result = [0] * (len(A) + 1)
    for i in xrange(1, len(A) + 1):
        result[i] = result[i - 1] + A[i - 1]
    return result


def getWays(squares, d, m):
    pref = get_prefix_sums(squares)
    ways = 0
    for i in xrange(len(squares) - m + 1):
        if pref[i + m] - pref[i] == d:
            ways += 1
    return ways


n = int(raw_input().strip())
s = map(int, raw_input().strip().split(' '))
d, m = raw_input().strip().split(' ')
d, m = [int(d), int(m)]
result = getWays(s, d, m)
print(result)
