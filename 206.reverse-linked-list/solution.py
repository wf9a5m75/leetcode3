# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = tail = ListNode()
        while(head):
            hNext = head.next

            head.next = root.next
            root.next = head

            head = hNext
        return root.next
