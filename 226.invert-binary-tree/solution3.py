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

        tree_stack: List[TreeNode] = [root]
        while tree_stack:
            tree = tree_stack.pop()

            # Swap the left and right children
            tree.left, tree.right = tree.right, tree.left

            # Append non-null children to the stack
            if tree.right:
                tree_stack.append(tree.right)
            if tree.left:
                tree_stack.append(tree.left)

        return root
