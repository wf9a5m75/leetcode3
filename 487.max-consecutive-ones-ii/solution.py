class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0
        L = Z = 0
        N = len(nums)
        hasZero = False

        for R in range(N):
            num = nums[R]
            if num == 0:
                if hasZero:
                    result = max(result, R - L)
                    L = Z + 1
                    Z = R
                else:
                    Z = R
                    hasZero = True

        result = max(result, N - L)
        return result
