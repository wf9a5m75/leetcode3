from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCounts = Counter(s)
        tCounts = Counter(t)
        return sCounts == tCounts
