func climbStairs(n int) int {
	dp := make([]int, 3)
	dp[0] = 1
	for i := 0; i < n; i++ {
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