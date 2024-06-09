class Solution:
    def partitionString(self, s: str) -> int:
        ordA = ord("a")
        N = len(s)
        count = 1
        memo = 0
        for char in s:
            
            bitMask = 1 << (ord(char) - ordA)
            
            if (memo & bitMask == 0):
                memo |= bitMask
                continue
                
            memo = bitMask
            count += 1
        return count