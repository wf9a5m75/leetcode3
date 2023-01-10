class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        if N == 1:
            return True

        maxJmp = 0
        i = 0
        while (i < N) and (i <= maxJmp) and (maxJmp < N):
            maxJmp = max(maxJmp, i + nums[i])
            i += 1
        return maxJmp >= N - 1
