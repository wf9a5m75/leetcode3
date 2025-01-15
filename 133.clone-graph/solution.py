"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

"""
DFS

V...number of verticles (nodes)
E...number of edges

Time: O(V + E)
Space: O(E)
"""
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        cache = {}

        def copyNode(node: Optional['Node']) -> Optional['Node']:
            if node is None:
                return None
            if node.val in cache:
                return cache[node.val]
            
            copied = Node(node.val)
            cache[node.val] = copied

            copied_neighbors = []
            for neighbor in node.neighbors:
                copied_neighbors.append(copyNode(neighbor))
            copied.neighbors = copied_neighbors
            
            return copied

        return copyNode(node)
