class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        length = len(s)
        centerPos = length >> 1
        
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        cntLeft = 0
        cntRight = 0
        pos = 0
        while (pos < centerPos):
            cntLeft += 1 if s[pos] in vowels else 0
            cntRight += 1 if s[centerPos + pos] in vowels else 0
            pos += 1
        return cntLeft == cntRight