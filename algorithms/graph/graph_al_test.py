class Vertex:
    def __init__(self, n):
        self.name = n

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

class Graph:
    def __init__(self):
        self.vertices = {}
        self.edges = {}

    def add_vertex(self, v):
        if isinstance(v, Vertex) and v.name not in self.vertices:
            self.vertices[v.name] = v
            self.edges[v.name] = []

    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            self.edges[u].append(self.vertices[v])

    def print_graph(self):
        print(self.edges)


    def bfs(self, s, callback):
        print('Level order graph traversal:')
        visited = set()
        queue = []
        queue.append(self.vertices[s])
        while queue:
            curr = queue.pop()
            callback(curr)
            visited.add(curr.name)
            for n in self.edges[curr.name]:
                if n.name not in visited:
                    queue.append(n)

    def color_graph(self):
        max_degree = max([len(n) for _, n in self.edges.items()])
        colors = ['c%s' % i for i in range(1, max_degree + 2)]
        node_colors = {}
        print('Max degree: %s' % max_degree)
        print('Colors: %s' % colors)
        for node_name in self.edges:
            self.bfs()

graph = Graph()
vertices = 'ABCDEFGH'
for v in vertices:
    graph.add_vertex(Vertex(v))

adjacency = ['AB', 'AC', 'CD', 'BC', 'DE', 'EF', 'FG', 'HC']
for a in adjacency:
    graph.add_edge(a[:1], a[1:])

#graph.print_graph()
#graph.bfs('A', lambda vertex: print(vertex))
graph.color_graph()
