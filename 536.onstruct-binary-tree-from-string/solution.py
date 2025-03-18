# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        if s == "":
            return None
        
        root = TreeNode()
        stack = [root]
        currNode = root
        n = len(s)
        i = 0
        sign = 1

        while i < n:
            char = s[i]

            if char == ")":
                topNode = stack.pop()
                if topNode.left:
                    topNode.right = currNode
                else:
                    topNode.left = currNode
                currNode = topNode
                i += 1
                continue

            if char == "(":
                stack.append(currNode)
                currNode = TreeNode()
                i += 1
                sign = 1
                continue
            
            if char == "-":
                currNode.val = int(s[i + 1]) * -1
                sign = -1
                i += 2
                continue

            currNode.val = currNode.val * 10 + int(char) * sign
            i += 1

        return root
