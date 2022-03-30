from es_tree import EsTree


#        0
#      /  \
#     1    2
#    / \     \
#   3   4  -  5

def main():
    e = EsTree(6, [(0,1), (0,2), (1,3), (1,4), (2,5), (4,5)], 0)
    print(e.distanceFromSource(0))
    print(e.distanceFromSource(1))
    print(e.distanceFromSource(2))
    print(e.distanceFromSource(3))
    print(e.distanceFromSource(4))
    print(e.distanceFromSource(5))
    e.deleteEdge(2,5)
    print(e.distanceFromSource(5))
    e.deleteEdge(0,2)
    print(e.distanceFromSource(2))
    print(e.distanceFromSource(5))
    e.deleteEdge(4,5)
    print(e.distanceFromSource(5))
    

if __name__ == "__main__":
    main()