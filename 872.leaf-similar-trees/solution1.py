# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.preorder(root1) == self.preorder(root2)
    
    def preorder(self, root: Optional[TreeNode]) -> List[int]:
        results = []
        q = []
        while(root or q):
            if (root is None):
                root = q.pop()
                
            if (root.left is None) and (root.right is None):
                results.append(root.val)
                root = None
                continue
            
            if (root.right):
                q.append(root.right)
                
            root = root.left
            
        return results