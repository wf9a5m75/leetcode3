class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem = {}
        for i, num in enumerate(nums):
            s = target - num
            if (s in mem):
                return [i, mem[s]]
            mem[num] = i

        return [0, 0]
