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
    fun oddEvenList(head: ListNode?): ListNode? {
        if (head?.next == null) {
            return head
        }
        val heads = arrayOf(
            ListNode(-1),
            ListNode(-1)
        )
        val pointers = arrayOf(
            heads[0],
            heads[1]
        )

        var idx = 0
        var _h = head
        while (_h != null) {
            pointers[idx].next = _h
            pointers[idx] = pointers[idx].next
            _h = _h?.next
            idx = (idx + 1) and 1
        }
        pointers[0].next = heads[1].next
        pointers[1].next = null
        // this.printList(heads[0])
        // this.printList(heads[1])
        return heads[0].next
    }

    fun printList(head: ListNode?) {
        var _h = head
        val strBuffer = StringBuffer()
        while (_h != null) {
            strBuffer.append("${_h.`val`}->")
            _h = _h?.next
        }
        strBuffer.append("[null]")
        println(strBuffer)
    }
}
