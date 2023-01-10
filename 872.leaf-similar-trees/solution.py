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
        stack = [root]
        while (stack):
            node = stack.pop()
            if (node.left is None) and (node.right is None):
                results.append(node.val)
            else:
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        return results
