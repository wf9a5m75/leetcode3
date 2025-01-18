# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None or root == p or root == q:
            return root
        
        leftHand = self.lowestCommonAncestor(root.left, p, q)
        rightHand = self.lowestCommonAncestor(root.right, p, q)
        if leftHand == None:
            return rightHand
        elif rightHand == None:
            return leftHand
        else:
            return root
