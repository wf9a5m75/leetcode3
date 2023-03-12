#
# using priority queue (minimum heap queue)
#  Time complexity: O(N log k) ... k denotes the number of linked list
#
#  Space complexity: O(k)
#    Since we just use ((int, int) * k) for the queue,
#    we can consider O(k)
#
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # Put all LinkedLists into the heap queue
        h = []
        for idx, listNode in enumerate(lists):
            if (listNode is None):
                continue

            # Since I can't put the linked list itself for some reasons,
            # put the list index instead.
            heapq.heappush(h, (listNode.val, idx))

        # Rebuild the list
        root = tail = ListNode(-1)
        while h:
            # Pick the smallest linked list
            val, idx = heapq.heappop(h)
            listNode = lists[idx]

            # skip the nodes if the same value.
            curr = listNode
            while (curr) and (curr.next) and (curr.next.val == val):
                curr = curr.next

            # Connect the tail.next to the list head.
            tail.next = listNode

            # Move the pointer to the end of the same values.
            tail = curr

            # If the list is still available, put it to the queue.
            if (curr.next is not None):

                # Don't forget to update the list.
                lists[idx] = curr.next

                heapq.heappush(h, (curr.next.val, idx))

        return root.next
