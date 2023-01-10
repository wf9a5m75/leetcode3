class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)

        INF = float('inf')
        dp = [INF] * (N + 2)
        dp[0] = 0
        dp[1] = 0

        for i in range(N):
            dp[i + 1] = min(dp[i + 1], dp[i] + cost[i])
            dp[i + 2] = min(dp[i + 2], dp[i] + cost[i])

        return dp[N]
