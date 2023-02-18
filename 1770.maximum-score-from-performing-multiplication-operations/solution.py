#
# TC: O(M * M)
# SC: O(M * M)
#
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        N = len(nums)
        M = len(multipliers)

        @cache
        def dp(mIdx: int, L: int) -> int:
            R = N - 1 - (mIdx - L)
            if (mIdx == M):
                return 0

            doLeft = nums[L] * multipliers[mIdx] + dp(mIdx + 1, L + 1)
            doRight = nums[R] * multipliers[mIdx] + dp(mIdx + 1, L)
            return max(doLeft, doRight)
        return dp(0, 0)
