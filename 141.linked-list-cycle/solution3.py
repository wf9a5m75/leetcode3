# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slower = head
        faster = head
        while faster and faster.next:
            faster = faster.next.next
            slower = slower.next
            if faster == slower:
                return True
        return False
