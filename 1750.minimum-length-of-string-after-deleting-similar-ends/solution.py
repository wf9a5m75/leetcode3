class Solution:
    def minimumLength(self, s: str) -> int:
        L = 0
        R = len(s) - 1
        while (L < R) and (s[L] == s[R]):
            char = s[L]
            L += 1
            R -= 1
            
            while (L < R) and (s[L] == char):
                L += 1
            
            while (L <= R) and (s[R] == char):
                R -= 1
        # print(L, R)
        return R - L + 1