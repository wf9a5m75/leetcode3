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
        p2, q2 = p, q
        while p2 != q2:
            p2 = p2.parent if p2 else q
            q2 = q2.parent if q2 else p
        return p2
