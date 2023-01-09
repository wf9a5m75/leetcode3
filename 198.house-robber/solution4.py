class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [0] * 3
        for i in range(N):
            dp[2] = nums[i] + dp[0]
            dp[1] = max(dp[1], dp[0])
            dp[0] = dp[1]
            dp[1] = dp[2]
        return max(dp[0], dp[1])
