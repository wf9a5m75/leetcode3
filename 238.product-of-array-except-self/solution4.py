class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        results = [1] * n
        
        prefix = 1
        suffix = 1
        for i in range(n):
            results[i] *= prefix
            prefix *= nums[i]
            results[n - i - 1] *= suffix
            suffix *= nums[n - i - 1]
        return results
