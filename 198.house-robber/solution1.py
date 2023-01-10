"""
    DP:
        TC: O(N)
        SC: O(N)
"""
class Solution:
    def rob(self, nums: List[int]) -> int:

        N = len(nums)
        dp = [0] * (N + 2)
        for i in range(N - 1, -1, -1):
            doNothing = dp[i + 1]
            doRobbering = dp[i + 2] + nums[i]
            dp[i] = max(doNothing, doRobbering)
        return dp[0]
