# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        result = 0
        root.val = 0
        q = [root]
        while(q):
            nextQ = []
            while(q):
                curr = q.pop()

                if (curr.left):
                    if (curr.left.left is None) and (curr.left.right is None):
                        result += curr.left.val
                    nextQ.append(curr.left)

                if (curr.right):
                    nextQ.append(curr.right)
            q = nextQ
        return result
                    
