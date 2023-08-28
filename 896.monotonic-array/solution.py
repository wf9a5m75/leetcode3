class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        numsLen = len(nums)
        if (numsLen == 1):
            return True
        
        # find the start position
        prevNum = nums[0]
        for i, num in enumerate(nums):
            delta = prevNum - num
            startIdx = i
            if (delta == 0):
                continue
            break
        
        for i in range(startIdx, numsLen - 1):
            delta2 = nums[i] - nums[i + 1]
            if (delta2 == 0):
                continue
            elif (delta > 0 and delta2 < 0) or (delta < 0 and delta2 > 0):
                return False
        return True