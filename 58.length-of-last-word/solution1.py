class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sLen = len(s)
        
        i = sLen - 1
        length = 0
        
        # skip tail spaces
        while (s[i] == " "):
            i -= 1
        
        # find the next space
        while (i >= 0) and (s[i] != " "):
            length += 1
            i -= 1
        return length