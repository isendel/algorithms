from functools import cmp_to_key


def solution(A):
    events = sorted([('s', i - a) for i, a in enumerate(A)] + [('e', i + a) for i, a in enumerate(A)],
                    key=cmp_to_key(event_comparator))
    curr_opened = 0
    result = 0
    for e in events:
        if e[0] == 's':
            result += curr_opened
            print('circle started at %s. Increasing result by %s. total: %s' % (e[1], curr_opened, result))
            curr_opened += 1
        if e[0] == 'e':
            curr_opened -= 1
            print('circle ended at %s. Left opened: %s' % (e[1], curr_opened))
        if result > 10000000:
            return -1
    return result


def event_comparator(x, y):
    if x[1] > y[1] or x[1] == y[1] and x[0] == 'e':
        return 1
    elif x[1] < y[1] or x[1] == y[1] and x[0] == 's':
        return -1
    else:
        return 0
