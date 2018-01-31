import numpy as np;

class Vertex:
    def __init__(self, n):
        self.name = n

    def __str__(self):
        return self.name

class Graph:
    def __init__(self):
        self.vertices = {}
        self.edges = None
        self.edge_indices = {}


    def add_vertex(self, v):
        if isinstance(v, Vertex) and v.name not in self.vertices:
            if len(self.vertices) == 0:
                self.edges = np.zeros((1,1))
            else:
                n = self.edges.shape[0]
                self.edges = np.append(self.edges, np.zeros((n, 1)), axis=1)
                self.edges = np.append(self.edges, np.zeros((1, n + 1)), axis=0)
            self.vertices[v.name] = v
            self.edge_indices[v.name] = self.edges.shape[0] - 1

    def add_edge(self, u, v, weight=1):
        if v in self.vertices and u in self.vertices:
            self.edges[self.edge_indices[u]][self.edge_indices[v]] = weight
        pass

    def print_graph(self):
        print(self.edges)

    def color_graph(self):
        _result = self.edges.copy()
        #_result
        print(_result)


g = Graph()
vertices = 'ABCDE'
for v in vertices:
    g.add_vertex(Vertex(v))

edges = ['AB', 'AC', 'BC', 'BD', 'CD', 'DE']
for e in edges:
    g.add_edge(e[:1], e[1:])
    g.add_edge(e[1:], e[:1])

g.print_graph()
g.color_graph()
