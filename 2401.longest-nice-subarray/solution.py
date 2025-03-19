class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        mask = 0
        longest = 0
        left = 0
        for right, num in enumerate(nums):
            if mask & num == 0:
                longest = max(longest, right - left + 1)
            else:
                while (mask & num > 0) and left < right:
                    mask = mask ^ nums[left]
                    left += 1
            mask = mask ^ num
        return longest
