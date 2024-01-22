from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        expectSum = (n * (n + 1)) >> 1
        s = 0
        results = [0, 0]
        memo = set()
        for i, num in enumerate(nums):
            s = s + num
            if (num in memo):
                results[0] = num
            memo.add(num)
        results[1] = (expectSum - s) + results[0]
        return results