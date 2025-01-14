# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
    
        def dfs(root):
            if root is None:
                return True, 0
            resultL, depthL = dfs(root.left)
            if not resultL:
                return False, 0

            resultR, depthR = dfs(root.right)
            if not resultR:
                return False, 0

            if (abs(depthL - depthR) < 2):
                return True, max(depthL, depthR) + 1
            else:
                return False, 0
        result, height = dfs(root)
        return result
