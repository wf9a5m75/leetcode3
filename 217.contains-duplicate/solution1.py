from collections import defaultdict
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        memo = defaultdict(int)
        for num in nums:
            memo[num] += 1
            if memo[num] == 2:
                return True
        return False
                