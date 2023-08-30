class Solution:
    def countOdds(self, low: int, high: int) -> int:
        result = 0
        if (low & 1) == 1:
            result += 1
            low += 1
        if (high & 1) == 1:
            result += 1
            high -= 1

        result += (high - low) >> 1
        return result
    
