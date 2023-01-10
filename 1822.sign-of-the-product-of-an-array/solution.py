class Solution:
    def arraySign(self, nums: List[int]) -> int:
        p = 1
        for num in nums:
            if num < 0:
                p *= -1
            elif num == 0:
                return 0
        return p
