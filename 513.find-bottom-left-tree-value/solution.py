# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        result = self.backtrack(root)
        return result[1]
    
    def backtrack(self, root: TreeNode):
        if (root.left is None) and (root.right is None):
            return [0, root.val]
        
        lResult = [0, 0]
        rResult = [0, 0]
        
        if (root.left is not None):
            lResult = self.backtrack(root.left)
            lResult[0] += 1
        if (root.right is not None):
            rResult = self.backtrack(root.right)
            rResult[0] += 1
        
        if (lResult[0] == rResult[0]):
            return lResult
        
        if (lResult[0] > rResult[0]):
            return lResult
        else:
            return rResult