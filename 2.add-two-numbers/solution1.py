# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(-1)
        tail = result
        carryUp = 0
        while (l1 or l2):
            s = carryUp
            s += 0 if l1 is None else l1.val
            s += 0 if l2 is None else l2.val
            
            node = ListNode(s % 10)
            tail.next = node
            tail = node
            carryUp = int(s / 10)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carryUp != 0:
            tail.next = ListNode(carryUp)
        
        return result.next