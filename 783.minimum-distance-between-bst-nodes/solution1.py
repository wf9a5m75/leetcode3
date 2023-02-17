#
# TC: O(N)
# SC: O(N)
#
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:

        buff = []

        def inorderTraversal(curr: Optional[TreeNode]):
            if (curr is None):
                return
            inorderTraversal(curr.left)
            buff.append(curr.val)
            inorderTraversal(curr.right)

        inorderTraversal(root)


        minDiff = float('inf')
        for i in range(1, len(buff)):
            minDiff = min(minDiff, buff[i] - buff[i - 1])
        return minDiff
