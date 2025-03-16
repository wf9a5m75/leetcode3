class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = -inf
        currSum = -inf
        for num in nums:
            currSum = max(num, currSum + num)
            result = max(result, currSum)
        return result
