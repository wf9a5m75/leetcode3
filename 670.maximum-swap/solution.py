class Solution:
    def maximumSwap(self, num: int) -> int:
        if num < 10:
            return num
        digits = []
        while num > 0:
            digits.insert(0, num % 10)
            num = int(num / 10)
        
        n = len(digits)
        maxIdx = [i for i in range(n)]
        maxIdx[n - 1] = n - 1
        for i in range(n - 2, -1, -1):
            if digits[maxIdx[i + 1]] >= digits[i]:
                maxIdx[i] = maxIdx[i + 1]
        
        result = 0
        found = False
        for i in range(n):
            if found == False and digits[maxIdx[i]] != digits[i]:
                digits[i], digits[maxIdx[i]] = digits[maxIdx[i]], digits[i]
                found = True
            
            result = result * 10 + digits[i]
        
        return result
