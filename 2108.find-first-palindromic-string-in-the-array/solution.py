class Solution:
    def isPalindrome(self, word: str) -> bool:
        L = 0
        R = len(word) - 1
        while (L < R) and (word[L] == word[R]):
            L += 1
            R -= 1
        return (L == R) or (R + 1 == L)
        
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if (self.isPalindrome(word)):
                return word
        return ""