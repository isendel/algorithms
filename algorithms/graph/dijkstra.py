'''Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function would be added by GfG's Online Judge.'''

# Your task is to complete this function
# The function prints V space separated integers where
# the ith integer denote the shortest distance of ith vertex
# from source vertex
import numpy as np
from collections import deque


def dijkstra(graph, v, s):
    # print(np.array(graph))
    N = len(graph)
    visited = [False] * v
    dist = [float('inf')] * v
    dist[s] = 0

    curr = s

    for _ in range(len(graph)):
        # select node with min dist
        min_dist = float('inf')
        next_node = s
        for i in range(N):
            if graph[curr][i] > 0 and dist[i] < min_dist:
                next_node = i

        curr = next_node
        # visited[curr] = True

        for i in range(N):
            if graph[curr][i] != 0:
                dist[i] = min(dist[i], dist[curr] + graph[curr][i])

    print(' '.join(map(str, dist)), end='')
