# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q = [root]
        results = []
        isL_to_R = True
        while (q):
            nextQ = []
            result = []
            while (q):
                curr = q.pop(0)
                if isL_to_R:
                    result.append(curr.val)
                else:
                    result.insert(0, curr.val)

                if curr.left:
                    nextQ.append(curr.left)
                if curr.right:
                    nextQ.append(curr.right)
            q = nextQ
            results.append(result)
            isL_to_R = not isL_to_R
        return results
                
