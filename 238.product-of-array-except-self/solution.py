class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        answers = [0] * N
        total = 1
        zeroCnt = 0
        zeroIdx = -1
        for i, num in enumerate(nums):
            if (num == 0):
                zeroCnt += 1
                zeroIdx = i
            else:
                total *= num
        if (zeroCnt == 1):
            answers[zeroIdx] = total
            
        if (zeroCnt > 0):
            return answers
        
        for i, num in enumerate(nums):
            answers[i] = int(total / num)
        
        return answers