class Solution {
    fun average(salary: IntArray): Double {
        var lowest = salary.min()!!.toDouble()
        var highest = salary.max()!!.toDouble()
        var total = salary.sum()!!.toDouble()
        return (total - highest - lowest) / (salary.size - 2).toDouble()
    }
}
