from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if (low > high) or (root is None):
            return 0

        result = 0
        if (low <= root.val) and (root.val <= high):
            result += root.val
        if (low < root.val):
            result += self.rangeSumBST(root.left, low, min(root.val - 1, high))
        if (high > root.val):
            result += self.rangeSumBST(root.right, max(low, root.val + 1), high)
        return result
