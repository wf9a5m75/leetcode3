#
# TC: O(N)
# SC: O(H) H denotes the maximum height of the tree
#     Recursive call takes O(H) stack.
#
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:

        global minDiff
        global prevValue
        prevValue = 10000
        minDiff = float('inf')

        def inorderTraversal(curr: Optional[TreeNode]):
            global minDiff
            global prevValue
            if (curr is None):
                return
            inorderTraversal(curr.left)
            minDiff = min(minDiff, abs(curr.val - prevValue))
            prevValue = curr.val

            inorderTraversal(curr.right)

        inorderTraversal(root)

        return minDiff
