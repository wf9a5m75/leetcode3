class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        results = []
        
        table = "123456789"
        for length in range(len(str(low)), len(str(high)) + 1):
            i = 0
            while (i + length < 10):
                val = int(table[i:i + length])
                if (low <= val <= high):
                    results.append(val)
                i += 1
        return results
        