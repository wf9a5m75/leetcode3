class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}
        for i, val in enumerate(nums):
            rest = target - val
            if (rest in memo):
                return [memo[rest], i]
            memo[val] = i
            