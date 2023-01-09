class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        N = len(s)
        if (N == 0):
            return 0
        mem = set()
        result = 0
        L = R = 0
        while (R < N):
            while (R < N) and (s[R] not in mem):
                mem.add(s[R])
                R += 1
            result = max(result, R - L)

            if (R < N):
                while (s[R] in mem):
                    mem.remove(s[L])
                    L += 1

        return result
