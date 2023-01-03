class Solution {
    fun minDeletionSize(strs: Array<String>): Int {
        var result = 0
        val M = strs.size
        val N = strs[0].length

        for (x in 0 until N) {
            var prev = -1
            for (y in 0 until M) {
                val cOrder = strs[y][x].toInt()
                if (prev <= cOrder) {
                    prev = cOrder
                    continue
                }
                result += 1
                break
            }
        }
        return result
    }
}
