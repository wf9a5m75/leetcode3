class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False

        counts = [0] * 26
        aOrd = ord("a")
        for char in s:
            idx = ord(char) - aOrd
            counts[idx] += 1
        for char in t:
            idx = ord(char) - aOrd
            counts[idx] -= 1

        for i in range(26):
            if (counts[i] != 0):
                return False
        return True
