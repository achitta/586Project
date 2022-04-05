from es_tree import EsTree
import math

class SCC:
    def __init__(self, vertices, edges, srcNode):
        self.es_normal = EsTree(vertices, edges, srcNode)
        reverse_edges = []
        for src, dst in edges:
            reverse_edges.append((dst, src,))
        self.es_reverse = EsTree(vertices, reverse_edges, srcNode)
        self.vertices = vertices
        print(self.es_normal.distanceFromSource(1))
        print(self.es_normal.distanceFromSource(2))
        print(self.es_normal.distanceFromSource(3))

        print(self.es_reverse.distanceFromSource(1))
        print(self.es_reverse.distanceFromSource(2))
        print(self.es_reverse.distanceFromSource(3))
        
    def deleteEdge(self, src, dst):
        self.es_normal.deleteEdge(src, dst)
        self.es_reverse.deleteEdge(dst, src)

        to_delete = []
        for n_id in self.vertices:
            reach_normal = self.es_normal.distanceFromSource(n_id)
            reach_reverse = self.es_reverse.distanceFromSource(n_id)
            print(n_id)
            print(reach_normal)
            print(reach_reverse)
            print()
        
            # If a node is no longer reachable then remove it from the scc
            if reach_normal == math.inf or reach_reverse == math.inf:
                to_delete.append(n_id)
        
        for n_id in to_delete:
            self.vertices.remove(n_id)

        # Return the nodes that no longer are a part of the SCC
        return to_delete
            
g = SCC([1,2,3],[(1,2),(2,1),(1,3),(3,2)], 1)
# breakpoint()
g.deleteEdge(1,3)
