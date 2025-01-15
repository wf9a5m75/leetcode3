# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        def validate(node: TreeNode, lower: int, upper: int) -> bool:
            if node.val < lower or node.val > upper:
                return False
            result = True
            if node.left:
                result = validate(node.left, lower, node.val - 1)
            if result and node.right:
                result = validate(node.right, node.val + 1, upper)
            return result
        
        return validate(root, -2 ** 31, 2 ** 31 - 1)
