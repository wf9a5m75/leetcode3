# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        heads = [
            ListNode(-1),  # Odd header
            ListNode(-1)   # Even header
        ]
        pointers = [
            heads[0],
            heads[1]
        ]
        idx = 0
        while (head):
            pointers[idx].next = head
            pointers[idx] = pointers[idx].next
            head = head.next
            idx = ((idx + 1) & 1)
        pointers[0].next = heads[1].next
        pointers[1].next = None
        return heads[0].next
            
