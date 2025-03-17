# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        node = root
        answer = inf
        answer_diff = inf
        while node:
            diff = abs(target - node.val)
            if answer_diff > diff:
                answer = node.val
                answer_diff = diff
            elif answer_diff == diff:
                # We need to the smallest value for the case if there are multiple answers".
                answer = min(answer, node.val)


            if target == node.val:
                break
            if target < node.val:
                node = node.left
            else:
                node = node.right
        return answer
