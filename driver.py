from es_tree import EsTree
from kosaraju import KosarajuGraph


#        0
#      /  \
#     1    2
#    / \     \
#   3   4  -  5

def main():
    e = EsTree([0,1,2,3,4,5], [(0,1), (0,2), (1,3), (1,4), (2,5), (4,5)], 0)
    print(e.distanceFromSource(0))
    print(e.distanceFromSource(1))
    print(e.distanceFromSource(2))
    print(e.distanceFromSource(3))
    print(e.distanceFromSource(4))
    print(e.distanceFromSource(5))
    print("==============================")
    e.deleteEdge(2,5)
    print(e.distanceFromSource(5))
    print("==============================")
    e.deleteEdge(0,2)
    print(e.distanceFromSource(2))
    print(e.distanceFromSource(5))
    print("==============================")
    e.deleteEdge(4,5)
    print(e.distanceFromSource(5))

    print("==============================")
    edges = [(0, 1), (0,2),(0,3),(1,4),(1,5),(2,1),(2,5), (3,5),(5,4)]
    e = EsTree([0,1,2,3,4,5], edges, 0)
    print(e.distanceFromSource(0))
    print(e.distanceFromSource(1))
    print(e.distanceFromSource(2))
    print(e.distanceFromSource(3))
    print(e.distanceFromSource(4))
    print(e.distanceFromSource(5))
    print("==============================")
    e.deleteEdge(0,1)
    print(e.distanceFromSource(0))
    print(e.distanceFromSource(1))
    print(e.distanceFromSource(2))
    print(e.distanceFromSource(3))
    print(e.distanceFromSource(4))
    print(e.distanceFromSource(5))
    print("==============================")
    g = KosarajuGraph([0,1,2,3,4,5,6,7], [(0,1),(1,2),(2,3),(2,4),(3,0),(4,5), (5,6), (6,4), (6,7)])
    sccs, subgraphs = g.get_scc()
    print(sccs)
    print(subgraphs)
    

if __name__ == "__main__":
    main()