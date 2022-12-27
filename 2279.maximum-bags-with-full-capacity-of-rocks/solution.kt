import java.util.PriorityQueue
import java.util.Comparator

class Solution {
    fun maximumBags(capacity: IntArray, rocks: IntArray, additionalRocks: Int): Int {
        val compatator = Comparator<Int> {a, b -> a - b}
        val hq = PriorityQueue(capacity.size, compatator)

        capacity.forEachIndexed { i, cap ->
            hq.add(cap - rocks[i])
        }

        var cnt = 0
        var remainRocks = additionalRocks
        while ((remainRocks > 0) && (!hq.isEmpty())) {
            val bag = hq.poll()
            if (remainRocks >= bag) {
                cnt++
            }
            remainRocks -= bag
        }

        return cnt
    }
}
