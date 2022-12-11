# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        stack = [(root, 1)]
        mostDepth = 1
        while (stack):
            node, depth = stack.pop()
            mostDepth = max(mostDepth, depth)
            if (node.right):
                stack.append((node.right, depth + 1))
            if (node.left):
                stack.append((node.left, depth + 1))
        return mostDepth
