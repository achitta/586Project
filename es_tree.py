from collections import deque, defaultdict
import math

class Node:
    def __init__(self, id):
        # String/Integer
        self.id = id

        # Integers
        self.level = -1
        self.parent = -1

        # Sets 
        self.nonNeighbors = set()
        self.unchecked = set()
    
    def __str__(self):
        return f"Node(\n\tid: {self.id},\n\tlevel: {self.level},\n\tparent: {self.parent},\
                \n\tnonNeighbors: {self.nonNeighbors},\n\tunchecked: {self.unchecked})\n"
    
    def __repr__(self) -> str:
        return self.__str__()
    
class EsTree:
    def __init__(self, vertices, edges, srcNode):
        """Initialize ES Tree."""
        # self.vertices = vertices
        self.adjacencyMatrix = defaultdict(set) # Map from node id to set of neighbor ids
        self.idToNode = {} # Map from node id to node object
        self.srcNode = srcNode # Source node id
        self.numVertices = len(vertices)
        
        # Create N nodes
        for n_id in vertices:
            self.idToNode[n_id] = Node(n_id)
        
        # Initialize graph
        for src, dst in edges:
            self.adjacencyMatrix[src].add(dst)

            # Add incoming neighbors to node unchecked set
            self.idToNode[dst].unchecked.add(src)

        self.computeLevels()
        self.selectParent()
        self.idToNode[srcNode].parent = srcNode

    def deleteEdge(self, src, dst):
        """Remove edge from graph and update data structures accordingly."""
        # breakpoint()
        assert src in self.adjacencyMatrix and dst in self.adjacencyMatrix[src]
        # Remove edge in adjacency matrix
        self.adjacencyMatrix[src].remove(dst)

        dstNode = self.idToNode[dst]
        if src in dstNode.nonNeighbors:
            dstNode.nonNeighbors.remove(src)
        if src in dstNode.unchecked:
            dstNode.unchecked.remove(src)
        if dstNode.parent == src:
            dstNode.parent = -1

        self.updateLevel(dstNode)

    def updateLevel(self, currNode: Node):
        """Update parent and level of node accordingly."""
        # Get the parent node
        # breakpoint()
        parentNode = None
        if currNode.parent != -1:
            parentNode = self.idToNode[currNode.parent]
        
        # If currNode has lost its parent, need to update
        if (currNode.parent == -1 or parentNode.level >= currNode.level) and currNode.id != self.srcNode:
            self.findNextParent(currNode)
            # If no parent can be found
            if currNode.parent == -1:
                # Move everything from nonNeighbors to unchecked
                for n_id in currNode.nonNeighbors:
                    currNode.unchecked.add(n_id)
                currNode.nonNeighbors.clear()

                # Increment level
                currNode.level += 1
                if currNode.level >= self.numVertices:
                    currNode.level = math.inf
                
                # Recursively call update level on neighbors
                if currNode.level != math.inf:
                    self.updateLevel(currNode)
                
                for n_id in self.adjacencyMatrix[currNode.id]:
                    neighbor = self.idToNode[n_id]
                    if neighbor.level != math.inf:
                        self.updateLevel(neighbor)       

    def findNextParent(self, currNode: Node):
        """Sets id of parent or -1 if no parent can be found."""
        toRemove = []
        parentFound = False
        for n_id in currNode.unchecked:
            neighbor = self.idToNode[n_id]
            # If this neighbor has a level that is >= current level
            # then we can confirm that this neighbor cannot serve as the
            # parent currently
            #
            # Else, make the node a parent of the current node
            toRemove.append(n_id)
            if neighbor.level >= currNode.level:
                currNode.nonNeighbors.add(n_id)
            else:
                currNode.parent = n_id
                parentFound = True
                break
        
        if not parentFound:
            currNode.parent = -1
        
        for n_id in toRemove:
            currNode.unchecked.remove(n_id)

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
    
    def distanceFromSource(self, node_id):
        if node_id == self.srcNode:
            return 0
        return self.idToNode[node_id].level