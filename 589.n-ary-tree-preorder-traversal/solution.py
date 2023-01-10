"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []

        result = []
        stack = [root]
        while (stack):
            curr = stack.pop()
            result.append(curr.val)
            while(curr.children):
                stack.append(curr.children.pop())

        return result
