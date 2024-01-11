# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        def traverse(node: Optional[TreeNode], minVal: int, maxVal: int) -> int:
            if (node is None):
                return maxVal - minVal
            minVal = min(minVal, node.val)
            maxVal = max(maxVal, node.val)
            
            return max(
                traverse(node.left, minVal, maxVal),
                traverse(node.right, minVal, maxVal)
            )
        return traverse(root, 100000, 0)