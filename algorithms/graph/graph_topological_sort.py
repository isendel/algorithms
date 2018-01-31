'''Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function would be added by GfG's Online Judge.'''


# Your task is to complete this function
# Function should return Topologically Sorted List
# Graph(graph) is a defaultict of type List
# n is no of edges

def topoSort(n, graph):
    if n == 0:
        return []
    elif n == 1:
        return graph.keys()

    visited = set()
    res_queue = []
    for v in graph:
        visit(v, visited, graph, res_queue)

    for i in range(n):
        if i not in visited:
            res_queue.append(i)
    return res_queue[::-1]


def visit(v, visited, graph, res):
    if v not in visited:
        for child in graph.get(v, []):
            visit(child, visited, graph, res)
        visited.add(v)
        res.append(v)
