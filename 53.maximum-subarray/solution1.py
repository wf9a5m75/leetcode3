class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefixSum = 0
        result = -inf
        for num in nums:
            prefixSum = max(prefixSum + num, num)
            result = max(result, prefixSum)
        return result