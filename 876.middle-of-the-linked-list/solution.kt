/**
 * Example:
 * var li = ListNode(5)
 * var v = li.`val`
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */
class Solution {
    fun middleNode(head: ListNode?): ListNode? {
        var fast: ListNode? = head!!.next
        if (fast == null) {
            return head
        }

        var slow: ListNode? = head!!

        while (fast != null) {
            fast = fast!!.next
            slow = slow!!.next
            if (fast != null) {
                fast = fast!!.next
            } else {
                break
            }
        }

        return slow
    }
}
