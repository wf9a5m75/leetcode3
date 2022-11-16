import kotlin.math.*
class Solution {
    fun average(salary: IntArray): Double {
        var lowest: Double = 10000000.0
        var highest: Double = 0.0
        var total: Double = 0.0

        for (s in salary) {
            var sD = s.toDouble()

            lowest = min(lowest, sD)
            highest = max(highest, sD)
            total += sD
        }
        return ((total - lowest - highest) / (salary.count() - 2))
    }
}
