class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sLen = len(s)
        
        # skip tail spaces
        R = sLen
        hitR = False
        for i in range(sLen - 1, -1, -1):
            if s[i] == " ":
                continue
            R = i
            hitR = True
            break
        
        # All characters are non-space
        if (hitR == False):
            return sLen
        
        # find the next space
        L = R
        hitL = False
        for j in range(R, -1, -1):
            if s[j] != " ":
                continue
            L = j
            hitL = True
            break
        if hitL == True:
            return R - L
        else:
            return R + 1