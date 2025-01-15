# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        results = []
        q = [root]
        while q:
            nextQ = []
            row = []
            while q:
                node = q.pop(0)
                row.append(node.val)
                if node.left:
                    nextQ.append(node.left)
                if node.right:
                    nextQ.append(node.right)
            q = nextQ
            results.append(row)
        return results