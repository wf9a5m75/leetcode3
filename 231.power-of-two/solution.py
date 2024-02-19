import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if (n < 1):
            return False
        if (n == 1):
            return True
        if (n & 1 == 1):
            return False
        result = math.log2(n)
        return result % 1 == 0