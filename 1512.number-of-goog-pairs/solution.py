from collections import defaultdict
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        result = 0
        for num in nums:
            result += counts[num]
            counts[num] += 1
        return result