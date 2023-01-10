class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [0] * (N + 2)
        for i in range(N):
            dp[i + 2] = nums[i] + dp[i]
            dp[i + 1] = max(dp[i + 1], dp[i])
        return max(dp[N], dp[N + 1])
