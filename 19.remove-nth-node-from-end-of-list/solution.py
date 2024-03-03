# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        pointer = head
        stack = []
        while (pointer):
            stack.append(pointer)
            pointer = pointer.next
        
        tail = None
        k = 0
        while (stack):
            k += 1
            last = stack.pop()
            if (n == k):
                continue
            last.next = tail
            tail = last
        return tail