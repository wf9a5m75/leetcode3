class Solution:
    def pivotInteger(self, n: int) -> int:
        if (n == 1):
            return 1
        summation = int((n * (n + 1)) / 2)
        
        L = 1
        R = n
        while (L < R):
            mid = (L + R) >> 1
            prefix = int((mid * (mid + 1)) / 2)
            suffix = summation - prefix + mid
            
            if (prefix == suffix):
                return mid
            elif (prefix < suffix):
                L = mid + 1
            else:
                R = mid - 1
        return -1
            