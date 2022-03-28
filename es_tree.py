

class Node:
    def __init__(self, id):
        # Integers
        self.id = id
        self.level = None
        self.parent = None

        # Sets 
        self.nonNeighbors = set()
        self.unchecked = set()
    
    def __str__(self):
        return f"Node(id: {self.id}, level: {self.level}, parent: {self.parent})"
    
    def __repr__(self) -> str:
        return self.__str__()
    
class EsTree:
    def __init__(self, numVertices, edges, srcNode):
        self.adjacencyMatrix = {}
        self.idToNode = {}
        
        # Init data structures
        for i in range(numVertices):
            self.adjacencyMatrix[i] = set()
            self.idToNode[i] = Node(i)
        
        for src, dst in edges:
            self.adjacencyMatrix[src].add(dst)
