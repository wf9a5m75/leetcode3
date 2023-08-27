"""
time complexity: O(n^2)
    because we use O(n) to make a copy of the s at `s[i:] + s[:i]`.
    We also O(n) to compair strings each other: the s and the t.
    So, O(n * 2n) = O(n * n) = O(n ^ 2)

space complexity: O(n)
    becase we make a copy of the s at `s[i:] + s[:i]`.
"""
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        lengthS = len(s)
        if (lengthS == 1):
            return False
        
        for i in range(1, lengthS):
            t = s[i:] + s[:i]
            if (s == t):
                return True
        return False