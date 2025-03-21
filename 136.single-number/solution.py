class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        zeroCnt = 0
        maskPositive = 0
        maskNegative = 0
        for num in nums:
            if num == 0:
                zeroCnt += 1
            elif num > 0:
                maskPositive = maskPositive ^ num
            else:
                maskNegative = maskNegative ^ -num
        
        if zeroCnt == 1:
            return 0
        elif maskPositive != 0:
            return maskPositive
        else:
            return -maskNegative
