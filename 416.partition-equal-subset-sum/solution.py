class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        
        half = total >> 1
        n = len(nums)
        dp = [[False] * (half + 1) for _ in range(n + 1)]

        dp[0][0] = True
        for i in range(1, n + 1):
            for j in range(half + 1):
                num = nums[i - 1]
                if j < num:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - num]
        return dp[n][half]
