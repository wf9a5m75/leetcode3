class Solution:
    def maxLength(self, words: List[str]) -> int:
        
        N = len(words)
        ordA = ord("a")
        
		    # Creates bitFlag conversion table
        bitFlagTables = [0] * 26
        prevFlag = 1
        for i in range(26):
            bitFlagTables[i] = prevFlag
            prevFlag <<= 1
        
		    # Since number of bits indicates the answer,
		    # we just need to keep all patterns of bit flags.
		
        dp = set([0])
        for word in words:
            
            # Create bitMask for the word
            wordBitMask = 0
            hasDupChars = 0
            for char in word:
                bitFlag = bitFlagTables[ord(char) - ordA]
                hasDupChars |= wordBitMask & bitFlag
                wordBitMask |= bitFlag
                
            # If there is no duplicated charactor in the word,
            # hasDupChars becomes zero
            if (hasDupChars > 0):
                continue
            
            nextDp = set()
            for bitFlags in dp:
                # Do nothing
                nextDp.add(bitFlags)
                
                # If there are common charactors, skip
                if (bitFlags & wordBitMask > 0):
                    continue
                
                # Merge ( = update the counts)
                nextDp.add(bitFlags | wordBitMask)
                
            dp = nextDp
        
        # Find the largest combination
        result = 0
        for bitFlag in dp:
            cnt = 0
            while (bitFlag > 0):
                cnt += bitFlag & 1
                bitFlag >>= 1
            result = max(result, cnt)
        return result