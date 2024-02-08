class Solution:
    def numSquares(self, n: int) -> int:
        MAX_INT = 10**4 + 1
        sqrtN = int(math.sqrt(n)) + 1
        dp = [MAX_INT] * (n + 1)
        dp[0] = 0
        
        for i in range(1, n + 1):
            for j in range(sqrtN):
                square = j * j
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i - square] + 1)
        return dp[n] 