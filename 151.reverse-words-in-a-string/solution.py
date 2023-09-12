class Solution:
    def reverseWords(self, s: str) -> str:
        sLen = len(s)
        
        # skip lead spaces
        i = 0
        while (i < sLen) and (s[i] == " "):
            i += 1
        
        j = i
        while (j < sLen) and (s[j] != " "):
            j += 1
        word = s[i: j]
        
        other = ""
        if (j < sLen):
            other = self.reverseWords(s[j:])
        if (other == ""):
            return word
        return f"{other} {word}"