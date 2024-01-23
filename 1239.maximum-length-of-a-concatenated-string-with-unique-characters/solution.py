class Solution:
    def maxLength(self, words: List[str]) -> int:
        
        N = len(words)
        
        @cache
        def backtrack(pos: int, buff: int) -> int:
            if (pos == N):
                
                cnt = 0
                bitMask = 1
                for i in range(26):
                    cnt += 1 if (bitMask & buff > 0) else 0
                    bitMask <<= 1
                return cnt
            
            doNothing = backtrack(pos + 1, buff)
            
            ordA = ord("a")
            for char in words[pos]:
                charBitFlag = 1 << (ord(char) - ordA)
                if (charBitFlag & buff > 0):
                    return doNothing
                
                buff |= charBitFlag
            
                
            doSomething = backtrack(pos + 1, buff) 
            return max(doSomething, doNothing)
        return backtrack(0, 0)