# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if (root is None):
            return 0

        def sumTree(soFar: int, curr: TreeNode) -> int:
            soFar = soFar * 10 + curr.val
            result = 0
            if (curr.left is None) and (curr.right is None):
                return soFar
            else:
                if curr.left:
                    result += sumTree(soFar, curr.left)
                if curr.right:
                    result += sumTree(soFar, curr.right)
                return result
        return sumTree(0, root)
