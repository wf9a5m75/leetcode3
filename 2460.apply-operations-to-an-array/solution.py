class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        zeroCnt = 0
        wIdx = 0
        for rIdx in range(n):
            if nums[rIdx] == 0:
                zeroCnt += 1
            else:
                nums[wIdx] = nums[rIdx]
                wIdx += 1
        
        for i in range(wIdx, n):
            nums[i] = 0
        return nums
