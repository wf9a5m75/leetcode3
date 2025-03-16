"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        pNodes = self.pathTo(p)
        qNodes = self.pathTo(q)

        pValues = [node.val for node in pNodes]
        
        for qNode in qNodes:
            if qNode.val in pValues:
                return qNode
    
    def pathTo(self, node: 'Node') -> List['Node']:
        result = []
        while node.parent:
            result.append(node)
            node = node.parent
        result.append(node)
        return result
