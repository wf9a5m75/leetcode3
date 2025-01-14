from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineFreq = Counter(magazine)
        noteFreq = Counter(ransomNote)

        for char, nFreq in noteFreq.items():
            mFreq = magazineFreq[char] or 0
            if nFreq > mFreq:
                return False
        return True
