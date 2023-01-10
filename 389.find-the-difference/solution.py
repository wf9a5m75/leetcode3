class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result = {}
        for c in t:
            result[c] = result.get(c, 0) + 1

        for c in s:
            result[c] -= 1

        for c in t:
            if result[c] == 1:
                return c
