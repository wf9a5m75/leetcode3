#
# TC: O(M * M)
# SC: O(M * M)
#

class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        N = len(nums)
        M = len(multipliers)
        dp = [0] * (M + 1)

        for mIdx in range(M - 1, -1, -1):
            for L in range(mIdx + 1):
                R = N - 1 - (mIdx - L)
                doLeft = nums[L] * multipliers[mIdx] + dp[L + 1]
                doRight = nums[R] * multipliers[mIdx] + dp[L]
                dp[L] = max(doLeft, doRight)

        return dp[0]
