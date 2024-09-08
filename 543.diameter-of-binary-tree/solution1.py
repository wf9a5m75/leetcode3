# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    
        self.longest = 0
        def traverse(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            left_depth = traverse(node.left)
            right_depth = traverse(node.right)
            diameter = left_depth + right_depth
            self.longest = max(self.longest, diameter)
            return max(left_depth, right_depth) + 1
        traverse(root)
        return self.longest
