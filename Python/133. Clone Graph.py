# Definition for a undirected graph node
# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        self.visited = {}
        return self.clone(node)
    
    def clone(self, node):
        if not node:
            return None
        if node.label in self.visited.keys():
            return self.visited[node.label]
        
        # create new node
        tmpNode = UndirectedGraphNode(node.label)
        # mark as visited
        self.visited[tmpNode.label] = tmpNode
        
        for neighbor in node.neighbors:
            tmpNode.neighbors.append(self.clone(neighbor))
        return tmpNode