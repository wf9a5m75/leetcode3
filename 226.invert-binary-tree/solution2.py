# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        # Swaps the left and right children
        root.left, root.right = root.right, root.left

        # Recursively invert the children
        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)
        return root
