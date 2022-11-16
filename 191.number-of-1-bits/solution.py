class Solution:
    def hammingWeight(self, n: int) -> int:
        numOfBits = 0
        while(n > 0):
            n &= n - 1
            numOfBits += 1

        return numOfBits
