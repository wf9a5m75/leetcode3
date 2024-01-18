class Solution {
    fun climbStairs(n: Int): Int {
        val dp = IntArray(3)
        dp[0] = 1
        for (i in 0..n) {
            dp[1] += dp[0]
            if (i + 2 <= n) {
                dp[2] = dp[0]
            }
            dp[0] = dp[1]
            dp[1] = dp[2]
            dp[2] = 0
        }
        return dp[0]
    }
}