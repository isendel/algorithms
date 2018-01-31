import numpy as np

class Vertex:
    def __init__(self, n):
        self.name = n

    def __str__(self):
        return self.name

class Graph:
    def __init__(self):
        self.vertices = {}
        self.edges = np.array([])
        self.edge_indices = {}

    def add_vertex(self, v):
        if isinstance(v, Vertex) and v.name not in self.vertices:
            self.vertices[v.name] = v
            for row in self.edges:
                row.append(0)
            self.edges.append([0] * (len(self.edges) + 1))
            self.edge_indices[v.name] = len(self.edges) - 1
            return True
        return False

    def add_edge(self, u, v, weight=1):
        if u in self.vertices and v in vertices:
           self.edges[self.edge_indices[u]][self.edge_indices[v]] = weight
        return False

    def print_graph(self):
        print('',', '.join(list(self.vertices.keys())))
        for row in self.edges:
            print(row)


graph = Graph()
vertices = 'ABCD'
for v in vertices:
    graph.add_vertex(Vertex(v))

edges = ['AB', 'AC', 'BC', 'BD', 'CD']
for e in edges:
    graph.add_edge(e[:1], e[1:])

graph.print_graph()
