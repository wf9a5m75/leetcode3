# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carryOver = 0
        result = tail = ListNode(-1)
        while(l1 and l2):
            s = l1.val + l2.val + carryOver
            tail.next = ListNode(s % 10)
            tail = tail.next
            carryOver = int(s / 10)
            l1 = l1.next
            l2 = l2.next

        remain = l1 or l2
        while(remain):
            s = remain.val + carryOver
            tail.next = ListNode(s % 10)
            tail = tail.next
            carryOver = int(s / 10)
            remain = remain.next

        if (carryOver > 0):
            tail.next = ListNode(carryOver)
        return result.next
