# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(-1)
        tail = head
        while (list1 and list2):
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
                tail = tail.next
                continue
            tail.next = list2
            list2 = list2.next
            tail = tail.next
        tail.next = list1 if list1 else list2
        return head.next
