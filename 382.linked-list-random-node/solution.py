# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        scope = 1
        chosen_value = 0
        curr = self.head

        #
        # (1/1) + (1/2) + (1/3) + ... + (1/n) = k/n
        # https://leetcode.com/problems/linked-list-random-node/solution/
        #
        while curr:
            if random.random() < 1 / scope:
                chosen_value = curr.val
            curr = curr.next
            scope += 1
        return chosen_value



# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
