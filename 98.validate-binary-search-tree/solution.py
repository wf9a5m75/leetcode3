# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        seen = set()
        def validation(curr: Optional[TreeNode], minVal: int, maxVal: int) -> bool:
            if (curr is None):
                return True
            if (minVal > curr.val) or (curr.val > maxVal) or (curr.val in seen):
                return False
            seen.add(curr.val)

            isLeftValid = False
            if (curr.left):
                if (curr.left.val < curr.val):
                    isLeftValid = validation(curr.left, minVal, curr.val - 1)
            else:
                isLeftValid = True

            isRightValid = False
            if (curr.right):
                if (curr.val < curr.right.val):
                    isRightValid = validation(curr.right, curr.val + 1, maxVal)
            else:
                isRightValid = True
            return isLeftValid and isRightValid

        return (validation(root.left, -float('inf'), root.val - 1) and
                validation(root.right, root.val + 1, float('inf')))
