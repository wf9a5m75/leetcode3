class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count = 0
        
        if high & 1 == 1:
            count += 1
            high -= 1
        
        if (low >= high):
            return count
        
        if low & 1 == 1:
            count += 1
            low += 1
        
        count += (high - low) >> 1
        return count