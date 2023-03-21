class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:

        nums.append(-1)
        result = 0
        consectiveZero = 0
        for num in nums:
            if num == 0:
                consectiveZero += 1
            else:
                result += (consectiveZero * (consectiveZero + 1)) >> 1
                consectiveZero = 0
        return result
