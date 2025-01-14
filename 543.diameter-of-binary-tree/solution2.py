# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0

        def traverse(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            left = traverse(root.left)
            right = traverse(root.right)
            diameter = left + right
            self.result = max(self.result, diameter)
            return max(left, right) + 1
        traverse(root)

        return self.result