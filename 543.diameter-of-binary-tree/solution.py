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
        self.traverse(root)
        return self.result
    
    def traverse(self, root: Optional[TreeNode]) -> int:
        if (root is None):
            return 0
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        self.result = max(self.result, left + right)
        return max(left, right) + 1