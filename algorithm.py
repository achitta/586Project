"""
Algorithm Steps:
1. Compute the SCCs - run Kosaraju
2. For each SCC select one of the nodes to serve as the root and build SCC object
3. If an edge deletion causes a breakdown in the SCC, then we need to recompute the SCCs for the current subgraph and continue with the algorithm
"""
from collections import defaultdict
import numpy as np
from scc import SCC
from kosaraju import KosarajuGraph

class Algorithm:
    def __init__(self, vertices, edges) -> None:
        self.all_sccs, self.all_subgraphs = self.computeScc(vertices, edges)

    def computeScc(self, vertices, edges):
        curr_sccs = []
        curr_subgraphs = []
        sccs, subgraphs = KosarajuGraph(vertices, edges).get_scc()
        for scc_vertices, scc_subgraph in zip(sccs, subgraphs):
            s = SCC(scc_vertices, scc_subgraph, np.random.choice(list(scc_vertices)))
            curr_sccs.append(s)
            curr_subgraphs.append(scc_subgraph)
        return curr_sccs, curr_subgraphs
    
    def deleteEdge(self, src, dst):
        idx = self.findScc(src, dst)
        if idx == -1:
            return
        curr_scc = self.all_sccs[idx]
        curr_subgraph = self.all_subgraphs[idx]
        curr_vertices = curr_scc.vertices.copy()
        
        # Delete edge from scc and from associated subgraph
        toDelete = curr_scc.deleteEdge(src, dst)
        
        deleteIndices = []
        for i, (e_src, e_dst,) in enumerate(curr_subgraph):
            if e_src in toDelete or e_dst in toDelete:
                deleteIndices.append((e_src, e_dst,))
        # Clean
        for deleteIndex in deleteIndices:
            curr_subgraph.remove(deleteIndex)

        new_all_sccs = []
        new_all_subgraphs = []
        # SCC is broken and we need to recompute
        if len(toDelete) > 0:
            new_sccs, new_subgraphs = KosarajuGraph(curr_vertices, curr_subgraph).get_scc()
            for scc_vertices, scc_subgraph in zip(new_sccs, new_subgraphs):
                if curr_scc.getRoot() in scc_vertices:
                    new_all_sccs.append(curr_scc)
                else:
                    new_root = np.random.choice(list(scc_vertices))
                    new_all_sccs.append(SCC(scc_vertices, scc_subgraph, new_root))
                    
                new_all_subgraphs.append(scc_subgraph)

            self.all_sccs.pop(idx)
            self.all_subgraphs.pop(idx)
            self.all_sccs.extend(new_all_sccs)
            self.all_subgraphs.extend(new_all_subgraphs)

    def findScc(self, src, dst):
        """Find the SCC and subgraph that contains some src and dst node and return index."""
        for idx, scc in enumerate(self.all_sccs):
            vertices = scc.getVertices()
            if src in vertices and dst in vertices:
                return idx
        return -1
    
    def getSccs(self):
        return [a.getVertices() for a in self.all_sccs], self.all_subgraphs
