# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def backtrack(node: TreeNode) -> List[int]:

            if (node.left is None) and (node.right is None):
                return [node.val, node.val, 0]

            maxDiff = 0
            minNum = maxNum = node.val
            if (node.left):
                other = backtrack(node.left)
                maxDiff = max(other[2], abs(node.val - other[0]), abs(node.val - other[1]))
                minNum = min(minNum, other[0])
                maxNum = max(maxNum, other[1])

            if (node.right):
                other = backtrack(node.right)
                maxDiff = max(maxDiff, other[2], abs(node.val - other[0]),  abs(node.val - other[1]))
                minNum = min(minNum, other[0])
                maxNum = max(maxNum, other[1])
            return [minNum, maxNum, maxDiff]

        result = backtrack(root)
        return result[2]
            
