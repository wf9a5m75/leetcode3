class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}
        for i, num in enumerate(nums):
            rest = target - num
            if rest in memo:
                return [memo[rest], i]
            memo[num] = i
