#
# TC: O(N log N)
# SC: O(N)
#
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        buff = [-1000000, 1000000]

        q = [root]
        while (q):
            curr = q.pop(0)

            L = 0
            R = len(buff) - 1
            while (L <= R):
                mid = (L + R) >> 1
                if (buff[mid] >= curr.val):
                    R = mid - 1
                else:
                    L = mid + 1
            buff.insert(L, curr.val)


            if (curr.left):
                q.append(curr.left)

            if (curr.right):
                q.append(curr.right)

        minDiff = float('inf')
        for i in range(1, len(buff) - 1):
            minDiff = min(minDiff, buff[i] - buff[i - 1])
        return minDiff
