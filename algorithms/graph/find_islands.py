'''Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function would be added by GfG's Online Judge.'''

# your task is to complete this function
# Your function should return an integer
from collections import defaultdict


def findIslands(arr, n, m):
    am = defaultdict(set)
    for i in range(n):
        for j in range(m):
            n_count = 0
            if arr[i][j] == 1:
                n_count += check_neighbor(arr, i, j, i - 1, j - 1, am, n, m)
                n_count += check_neighbor(arr, i, j, i, j - 1, am, n, m)
                n_count += check_neighbor(arr, i, j, i + 1, j - 1, am, n, m)
                n_count += check_neighbor(arr, i, j, i + 1, j, am, n, m)

                n_count += check_neighbor(arr, i, j, i + 1, j + 1, am, n, m)
                n_count += check_neighbor(arr, i, j, i, j + 1, am, n, m)
                n_count += check_neighbor(arr, i, j, i - 1, j + 1, am, n, m)
                n_count += check_neighbor(arr, i, j, i - 1, j, am, n, m)

                if n_count == 0:
                    am[get_node_name(i, j)] = set()
    visited = set()
    queue = []
    islands_count = 0
    for node in am.keys():
        if node not in visited:
            islands_count += 1
            queue.append(node)
            while len(queue) > 0:
                current_node = queue.pop()
                visited.add(current_node)
                for n in am[current_node]:
                    if n not in visited:
                        queue.append(n)

    return islands_count


def check_neighbor(arr, i, j, n_i, n_j, am, n, m):
    if 0 <= n_i < n and 0 <= n_j < m and arr[n_i][n_j] == 1:
        am[get_node_name(i, j)].add(get_node_name(n_i, n_j))
    return 0


def get_node_name(i, j):
    return str(i) + '_' + str(j)
