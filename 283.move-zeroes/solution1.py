class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        L = 0
        for R in range(len(nums)):
            nums[L] = nums[R]
            if (nums[R] == 0):
                continue
            L += 1
        for R in range(L, len(nums)):
            nums[R] = 0