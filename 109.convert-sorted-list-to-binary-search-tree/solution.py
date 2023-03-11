# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if (head is None):
            return None

        values = []

        def toBST(L: int, R: int) -> TreeNode:
            if (L > R):
                return None

            mid = (L + R) >> 1
            curr = TreeNode(values[mid])
            curr.left = toBST(L, mid - 1)
            curr.right = toBST(mid + 1, R)
            return curr

        while (head):
            values.append(head.val)
            head = head.next

        root = toBST(0, len(values) - 1)
        return root
