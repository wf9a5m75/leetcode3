class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        N = len(nums)
        if (N <= 1):
            return nums 
        
        half = N >> 1
        left = self.sortArray(nums[:half])
        right = self.sortArray(nums[half:])
        result = []
        
        L = 0
        R = 0
        INT_MAX = 2**31 - 1
        while L < half or R + half < N:
            valL = left[L] if (L < half) else INT_MAX
            valR = right[R] if (R + half < N) else INT_MAX
            if (valL <= valR):
                result.append(valL)
                L += 1
            else:
                result.append(valR)
                R += 1
        return result
        