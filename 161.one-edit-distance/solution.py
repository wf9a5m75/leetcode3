class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        shortN = len(s)
        longN = len(t)
        if (shortN > longN):
            return self.isOneEditDistance(t, s)

        if (longN - shortN > 1):
            return False

        for i in range(shortN):
            if (s[i] != t[i]):
                # if strings have the same length
                if (shortN == longN):
                    return s[i + 1:] == t[i + 1:]

                # if strings have different lengths
                else:
                    return s[i:] == t[i + 1:]
        # if there is no diffs on shortN distance,
        # the strings are one edit away only if
        # t has one more character.
        return shortN + 1 == longN
