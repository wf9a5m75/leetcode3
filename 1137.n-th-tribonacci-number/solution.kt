class Solution {
    fun tribonacci(n: Int): Int {
        var dp = mutableListOf(0, 1, 1)
        if (n < 3) {
            return dp[n]
        }

        for (i in 3..n) {
            val dp0 = dp[0]
            val dp1 = dp[1]
            dp[0] = dp[1]
            dp[1] = dp[2]
            dp[2] += dp0 + dp1
        }
        return dp[2]
    }
}
