from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if (len(word1) != len(word2)):
            return False
        
        counts1 = Counter(word1)
        counts2 = Counter(word2)
        if (counts1.keys() != counts2.keys()):
            return False
        values1 = list(sorted(counts1.values()))
        values2 = list(sorted(counts2.values()))
        return values1 == values2
        