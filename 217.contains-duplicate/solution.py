class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        prev = float('inf')
        for num in nums:
            if (prev == num):
                return True
            prev = num
        return False
