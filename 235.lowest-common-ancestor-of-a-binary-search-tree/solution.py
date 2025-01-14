# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# H denotes the height of tree
#
# Time complexity : O(log(2 ^ H))=O(H)
# Space complexity: O(H)

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path_p = self.findX(root, p.val)
        path_q = self.findX(root, q.val)

        lca = root
        while path_p and path_q and path_p[0].val == path_q[0].val:
            lca = path_p.pop(0)
            path_q.pop(0)
        return lca

    def findX(self, root: 'TreeNode', target: int) -> List['TreeNode']:
        path = []
        node = root
        while node:
            path.append(node)
            if node.val == target:
                return path
            if node.val < target:
                node = node.right
            else:
                node = node.left
        return []