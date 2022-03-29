from collections import deque

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
        return f"Node(\n\tid: {self.id},\n\tlevel: {self.level},\n\tparent: {self.parent},\
                \n\tnonNeighbors: {self.nonNeighbors},\n\tunchecked: {self.unchecked})\n"
    
    def __repr__(self) -> str:
        return self.__str__()
    
class EsTree:
    def __init__(self, numVertices, edges, srcNode):
        """Initialize ES Tree."""
        self.adjacencyMatrix = {} # Map from node id to set of neighbor ids
        self.idToNode = {} # Map from node id to node object
        self.srcNode = srcNode # Source node id
        
        for i in range(numVertices):
            self.adjacencyMatrix[i] = set()
            
            # Create node
            self.idToNode[i] = Node(i)
        
        for src, dst in edges:
            self.adjacencyMatrix[src].add(dst)

            # Add incoming neighbors to node unchecked set
            self.idToNode[dst].unchecked.add(src)

        self.computeLevels()
        self.selectParent()

    def computeLevels(self):
        """Computes and sets level for each node."""
        queue = deque()
        queue.append((self.srcNode, 0))
        visited = {self.srcNode}
        
        while queue:
            currId, currLevel = queue.popleft()
            self.idToNode[currId].level = currLevel

            for neighbor in self.adjacencyMatrix[currId]:
                if neighbor not in visited:
                    queue.append((neighbor, currLevel + 1))
                    visited.add(neighbor)
    
    def selectParent(self):
        """Select a parent for each node from unchecked set."""
        for _, node in self.idToNode.items():
            if node.unchecked:
                # Move an incoming node as parent
                node.parent = node.unchecked.pop()
            