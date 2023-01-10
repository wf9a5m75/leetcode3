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
    fun getDecimalValue(head: ListNode?): Int {
        var result = 0
        var pointer = head

        while (pointer != null) {
            result = (result shl 1) or pointer.`val`
            pointer = pointer.next
        }
        return result
    }
}
