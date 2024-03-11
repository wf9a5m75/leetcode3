# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        frequencies = {}
        result = None
        while head:
            nextNode = head.next
            val = head.val
            
            head.next = None
            if (val not in frequencies):
                node = ListNode()
                node.next = result
                result = node
                frequencies[val] = node
                
            
            frequencies[val].val += 1
            head = nextNode
        
        return result
        
        