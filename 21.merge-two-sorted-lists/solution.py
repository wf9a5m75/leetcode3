# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        root = tail = ListNode()
        while(list1) and (list2):

            val1 = list1.val
            val2 = list2.val
            if (val1 < val2):
                tail.next = list1
                while(list1) and (list1.val == val1):
                    tail = tail.next
                    list1 = list1.next
            else:
                tail.next = list2
                while(list2) and (list2.val == val2):
                    tail = tail.next
                    list2 = list2.next
        tail.next = list1 if list1 else list2
        return root.next
