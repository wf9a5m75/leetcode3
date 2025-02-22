class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            rest = target - num
            if rest in seen:
                return [seen[rest], i]
            seen[num] = i
