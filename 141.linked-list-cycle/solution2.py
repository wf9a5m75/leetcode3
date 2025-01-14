# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        faster, slower = head, head.next
        if faster is None:
            return False
        faster = faster.next

        while faster:
            faster = faster.next
            if faster:
                faster = faster.next
            if faster is None:
                return False
            
            faster = faster.next
            slower = slower.next
            if faster == slower:
                return True
        return False