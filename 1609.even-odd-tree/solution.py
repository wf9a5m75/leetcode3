# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        isOddLevel = True
        while (q):
            prev = q.popleft()
            if ((isOddLevel and (prev.val & 1 == 0)) or 
                (not isOddLevel and (prev.val & 1 == 1))):
                return False
                
            nextQ = deque()
            if (prev.left):
                nextQ.append(prev.left)
            if (prev.right):
                nextQ.append(prev.right)
            
            while (q):
                node = q.popleft()
                if ((isOddLevel) and ((prev.val >= node.val) or (node.val & 1 == 0))):
                    return False
                    
                if (not isOddLevel and ((prev.val <= node.val) or (node.val & 1 == 1))):
                    return False
                
                prev = node
                if (node.left):
                    nextQ.append(node.left)
                if (node.right):
                    nextQ.append(node.right)
            q = nextQ
            isOddLevel = not isOddLevel
        return True
    
        