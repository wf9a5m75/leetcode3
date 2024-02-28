"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        self.result = 0
        self.traverse(root)
        return self.result
        
    def traverse(self, root: 'Node') -> int:
        if (len(root.children) == 0):
            return 1
        results = []
        for child in root.children:
            results.append(self.traverse(child))
        if (len(results) == 1):
            self.result = max(self.result, results[0])
            return results[0] + 1
        
        results.sort(reverse = True)
        self.result = max(self.result, results[0] + results[1])
        return results[0] + 1