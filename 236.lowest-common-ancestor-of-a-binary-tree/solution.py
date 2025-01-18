# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pPath = self.findX(root, p)
        qPath = self.findX(root, q)
        lastNode = root
        for i in range(min(len(pPath), len(qPath))):
            if pPath[i] == qPath[i]:
                lastNode = pPath[i]
            else:
                break
        
        return lastNode

    def print(self, path: List['TreeNode']):
        result = "->".join(list(map(lambda node: str(node.val), path)))
        print(result)

    def findX(self, root: 'TreeNode', target: 'TreeNode') -> List['TreeNode']:
        path = []
        
        def traverse(node: 'TreeNode') -> bool:
            if node is None:
                return False
            path.append(node)
            if node == target:
                return True

            result = False
            if node.left:
                result = traverse(node.left)
            if result == False and node.right:
                result = traverse(node.right)
            if result == False:
                path.pop()
            return result
        traverse(root)
        return path
