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
    fun addTwoNumbers(l1: ListNode?, l2: ListNode?): ListNode? {
        val result = ListNode(-1)
        var tail = result

        var carryUp: Int = 0
        var s = 0
        var _l1 = l1
        var _l2 = l2
        while ((_l1 != null) || (_l2 != null)) {
            s = (_l1?.`val` ?: 0) + (_l2?.`val` ?: 0) + carryUp
            tail.next = ListNode(s % 10)
            tail = tail.next
            carryUp = s / 10
            _l1 = _l1?.next
            _l2 = _l2?.next
        }
        if (carryUp > 0) {
            tail.next = ListNode(carryUp)
        }
        return result.next
    }
}
