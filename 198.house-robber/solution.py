#
# Backtracking:
#   Time: O(N)
#   Space: O(N)
#
from functools import lru_cache
class Solution:
    def rob(self, nums: List[int]) -> int:

        N = len(nums)
        @lru_cache
        def backtrack(i: int) -> int:
            if (i >= N):
                return 0
            doNothing = backtrack(i + 1)
            doRobbering = backtrack(i + 2) + nums[i]
            return max(doNothing, doRobbering)
        return backtrack(0)
