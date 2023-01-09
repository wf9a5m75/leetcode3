class Solution {
    fun deleteAndEarn(nums: IntArray): Int {
        var lowest = 10001
        var highest = 0
        var counts = HashMap<Int, Int>()
        for (num in nums) {
            lowest = minOf(lowest, num)
            highest = maxOf(highest, num)
            counts[num] = (counts[num] ?: 0) + 1
        }

        val N = highest - lowest + 1
        val dp = IntArray(3)
        var num = lowest
        for (i in 0 .. N - 1) {
            dp[2] = dp[0] + num * (counts[num] ?: 0)
            dp[1] = maxOf(dp[1], dp[0])
            dp[0] = dp[1]
            dp[1] = dp[2]
            num += 1
        }
        return maxOf(dp[0], dp[1], dp[2])
    }
}
