from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        
        result = 0
        hasOneCharacter = False
        for key, cnt in counts.items():
            if cnt % 2 == 0:
                result += cnt
            elif hasOneCharacter == False:
                result += cnt
                hasOneCharacter = True
            else:
                result += cnt - 1
        return result