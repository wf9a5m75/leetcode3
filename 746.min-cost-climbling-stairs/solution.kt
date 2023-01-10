class Solution {
    fun minCostClimbingStairs(cost: IntArray): Int {
        val N = cost.size
        val dp = IntArray(N + 2)
        dp.fill(Int.MAX_VALUE)
        dp[0] = 0
        dp[1] = 0
        for (i in 0 until N) {
            dp[i + 1] = minOf(dp[i + 1], dp[i] + cost[i])
            dp[i + 2] = minOf(dp[i + 2], dp[i] + cost[i])
        }
        return dp[N]
    }
}
