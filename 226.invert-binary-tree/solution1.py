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
            return root

        left_tree = root.left
        right_tree = root.right
        if left_tree:
            root.right = self.invertTree(left_tree)
        else:
            root.right = None
        if right_tree:
            root.left = self.invertTree(right_tree)
        else:
            root.left = None
        return root
