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
        if (head == null) {
            return null
        }
        var faster = head
        var slower = head
        while ((faster != null) && (faster.next != null)) {
            faster = faster.next.next
            slower = slower!!.next
        }
        return slower
    }
}
