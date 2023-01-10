class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        i = 0
        len1, len2 = len(word1), len(word2)
        while (i < len1) and (i < len2):
            result += word1[i] + word2[i]
            i += 1
        if (i < len1):
            result += word1[i:]
        elif (i < len2):
            result += word2[i:]
        return result
