# Algorithm is to run Kosaraju on the graph after every deletion
from kosaraju import KosarajuGraph

class NaiveAlgorithm:
    def __init__(self, vertices, edges) -> None:
        self.vertices = vertices
        self.edges = edges
        self.all_sccs, self.all_subgraphs = self.computeScc(vertices, edges)

    def computeScc(self, vertices, edges):
        sccs, subgraphs = KosarajuGraph(vertices, edges).get_scc()
        return sccs, subgraphs
    
    def deleteEdge(self, src, dst):
        deleteIndex = -1
        for idx, (e_src, e_dst,) in enumerate(self.edges):
            if e_src == src and e_dst == dst:
                deleteIndex = idx
                break
        assert deleteIndex != -1
        self.edges.pop(deleteIndex)
        self.all_sccs, self.all_subgraphs = self.computeScc(self.vertices, self.edges)
    
    def getSccs(self):
        return self.all_sccs, self.all_subgraphs