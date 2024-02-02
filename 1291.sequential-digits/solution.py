class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        results = []
        
        for firstDigit in range(1, 10):
            
            digit = firstDigit
            val = 0
            while (val <= high) and (digit < 10):
                val = val * 10 + digit
                digit += 1
                if (val < low) or (val > high):
                    continue
                results.append(val)
                
        results.sort()
        return results