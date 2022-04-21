from collections import defaultdict

class KosarajuGraph:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.numVertices = len(vertices)
        self.graph = {}
        self.init_graph(vertices, edges)

    def init_graph(self, vertices, edges):
        for vertex in vertices:
            self.graph[vertex] = set()

        for src, dst in edges:
            self.add_edge(src, dst)
    
    # Add edge into the graph
    def add_edge(self, s, d):
        self.graph[s].add(d)

    # dfs
    def dfs(self, d, visited_vertex, current):
        visited_vertex.add(d)

        current.add(d)
        for i in self.graph[d]:
            if i not in visited_vertex:
                self.dfs(i, visited_vertex, current)

    def fill_order(self, d, visited_vertex, stack):
        visited_vertex.add(d)
        for i in self.graph[d]:
            if i not in visited_vertex:
                self.fill_order(i, visited_vertex, stack)
        stack = stack.append(d)

    # transpose the matrix
    def transpose(self):
        edges = []
        for i in self.graph:
            for j in self.graph[i]:
                edges.append((j, i,))
        g = KosarajuGraph(self.vertices, edges)

        return g

    # Return stongly connected components
    def get_scc(self):
        stack = []
        visited_vertex = set()
        vertices = self.graph.keys()
        for i in vertices:
            if i not in visited_vertex:
                self.fill_order(i, visited_vertex, stack)

        gr = self.transpose()

        visited_vertex = set()
        SCCs = []
        while stack:
            i = stack.pop()
            if i not in visited_vertex:
                current = set()
                gr.dfs(i, visited_vertex, current)
                SCCs.append(current)

        all_edges = []
        for scc in SCCs:
            edges = []
            for node in scc:
                outgoing = self.graph[node]
                for dst in outgoing:
                    if dst in scc:
                        # Reverse order because self.graph has reversed edges
                        edges.append((node, dst,)) 
            all_edges.append(edges)

        return SCCs, all_edges