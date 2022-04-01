from collections import defaultdict

current = set()
SCCs = []

class KosarajuGraph:
    def __init__(self, numVertices, edges):
        self.numVertices = numVertices
        self.graph = defaultdict(list)
        self.init_graph(edges)

    def init_graph(self, edges):
        for src, dst in edges:
            self.add_edge(src, dst)
    
    # Add edge into the graph
    def add_edge(self, s, d):
        self.graph[s].append(d)

    # dfs
    def dfs(self, d, visited_vertex):
        visited_vertex[d] = True

        current.add(d)

        for i in self.graph[d]:
            if not visited_vertex[i]:
                self.dfs(i, visited_vertex)

    def fill_order(self, d, visited_vertex, stack):
        visited_vertex[d] = True
        for i in self.graph[d]:
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)
        stack = stack.append(d)

    # transpose the matrix
    def transpose(self):
        edges = []
        for i in self.graph:
            for j in self.graph[i]:
                edges.append((j, i,))
        g = KosarajuGraph(self.numVertices, edges)

        return g

    # Print stongly connected components
    def get_scc(self):
        stack = []
        visited_vertex = [False] * (self.numVertices)

        for i in range(self.numVertices):
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)

        gr = self.transpose()

        visited_vertex = [False] * (self.numVertices)

        while stack:
            i = stack.pop()
            if not visited_vertex[i]:
                gr.dfs(i, visited_vertex)
                SCCs.append(current.copy())
                current.clear()
        return SCCs