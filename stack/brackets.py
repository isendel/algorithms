# Check if brackets in the string are in correct open/close order
from collections import deque
def solution(S):
    mapping = {'(':')', '[':']', '{':'}'}
    p = deque()
    result = 1
    if len(S) == 0:
        return 1
    for i in xrange(len(S)):
        if S[i] in ['(', '{', '[']:
            p.append(S[i])
        else:
            result &= len(p) > 0 and (mapping[p.pop()] == S[i])
    return 1 if result == 1 and len(p) == 0 else 0
