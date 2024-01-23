class Solution:
    def maxLength(self, words: List[str]) -> int:
        
        N = len(words)
        
        def dfs(pos: int, charsSoFar: int) -> int:
            if (pos == N):
                cnt = 0
                bitMask = 1
                for i in range(26):
                    cnt += 1 if (bitMask & charsSoFar > 0) else 0
                    bitMask <<= 1
                return cnt
            
			# If we don't use the current word, just move on to the next
            doNothing = backtrack(pos + 1, charsSoFar)
            
			# Detects words[pos] and charsSoFar has any common charactors in both.
            ordA = ord("a")
            for char in words[pos]:
                charBitFlag = 1 << (ord(char) - ordA)
				
				# We can't use this word
                if (charBitFlag & charsSoFar > 0):
                    return doNothing
                
                charsSoFar |= charBitFlag
            
            # We can use this word. 
            doSomething = backtrack(pos + 1, charsSoFar) 
			
			# Chooses the larger result
			return max(doSomething, doNothing)
			
        return dfs(0, 0)