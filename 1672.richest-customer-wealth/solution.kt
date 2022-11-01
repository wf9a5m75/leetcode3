class Solution {
    fun maximumWealth(accounts: Array<IntArray>): Int {
        var richest: Int = 0

        for (row in accounts) {
            richest = kotlin.math.max(richest, this.sumArr(row))
        }
        return richest
    }

    fun sumArr(arr: IntArray): Int {
        var s = 0
        for (num in arr) {
            s += num
        }
        return s
    }
}
