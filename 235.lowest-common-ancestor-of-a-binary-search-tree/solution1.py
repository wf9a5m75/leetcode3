
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val == q.val:
            return p
        
        if p.val > q.val:
            p, q = q, p
        
        if (p.val <= root.val) and (root.val <= q.val):
            return root
        
        if (p.val <= root.val) and (q.val <= root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)
