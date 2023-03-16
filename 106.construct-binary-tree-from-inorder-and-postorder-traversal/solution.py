# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        mem1 = {}
        for i, value in enumerate(inorder):
            mem1[value] = i

        def buildTree(
            inL: int, inR: int,
        ) -> Optional[TreeNode]:

            if (inL > inR):
                return None

            value = postorder.pop()
            node = TreeNode(value)
            idx1 = mem1[value]

            node.right = buildTree(idx1 + 1, inR)
            node.left = buildTree(inL, idx1 - 1)

            return node

        N = len(inorder)

        return buildTree(
            0, N - 1,
        )
