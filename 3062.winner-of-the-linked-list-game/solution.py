# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        
        points = [0, 0] # the points of even, odd teams
        while head:
            even = head.val
            odd = head.next.val
            head = head.next.next
            
            if (even == odd):
                continue
            
            idx = 0 if even > odd else 1
            points[idx] += 1
        
        if points[0] > points[1]:
            return "Even"
        elif points[0] < points[1]:
            return "Odd"
        else:
            return "Tie"