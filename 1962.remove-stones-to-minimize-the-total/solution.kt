import java.util.PriorityQueue
import java.util.Comparator

class Solution {
    fun minStoneSum(piles: IntArray, k: Int): Int {
        val hq = PriorityQueue<Int>(piles.size, Comparator<Int> { a, b -> b - a })

        // Build a max heap queue
        var total = 0
        for (pile in piles) {
            total += pile
            hq.add(pile)
        }

        // Do operations k times
        repeat(k) {
            var peek = hq.poll()
            val remove = peek / 2
            total -= remove
            peek -= remove
            hq.add(peek)
        }

        return total
    }
}
