class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1, 0, 0]
        
        for i in range(n):
            dp[1] += dp[0]
            
            if (i + 2 <= n):
                dp[2] += dp[0]
            
            dp[0] = dp[1]
            dp[1] = dp[2]
            dp[2] = 0
        return dp[0]