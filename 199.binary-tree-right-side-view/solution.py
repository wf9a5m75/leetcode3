# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        q = [root]
        
        result = []
        while q:
            last = None
            nextQ = []
            while q:
                curr = q.pop(0)
                last = curr.val
                if curr.left:
                    nextQ.append(curr.left)
                if curr.right:
                    nextQ.append(curr.right)
            result.append(last)
            q = nextQ
        return result
