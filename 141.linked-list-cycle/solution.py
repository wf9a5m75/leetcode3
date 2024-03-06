# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        faster = slower = head
        
        while (faster) and (faster.next):
            faster = faster.next
            if (faster.next is None):
                break
            faster = faster.next
            slower = slower.next
            if (faster == slower):
                return True
        return False