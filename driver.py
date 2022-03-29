from es_tree import EsTree


#        0
#      /  \
#     1    2
#    / \     \
#   3   4  -  5

def main():
    e = EsTree(6, [(0,1), (0,2), (1,3), (1,4), (2,5), (4,5)], 0)

if __name__ == "__main__":
    main()