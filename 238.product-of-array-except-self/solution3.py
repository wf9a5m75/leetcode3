class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        results = [0] * n
        zeroCnt = 0
        zeroIdx = 0
        total = 1
        for i, num in enumerate(nums):
            if num == 0:
                zeroCnt += 1
                zeroIdx = i
                continue
            total *= num
        
        if zeroCnt > 1:
            return results
        if zeroCnt == 1:
            results[zeroIdx] = total
            return results
        
        for i in range(n):
            results[i] = int(total / nums[i])
        return results
