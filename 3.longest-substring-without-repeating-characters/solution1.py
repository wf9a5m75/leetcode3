class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        N = len(s)
        L = 0
        R = 0
        
        appear = set()
        maxLen = 0
        while (R < N):
            while(R < N) and (s[R] not in appear):
                appear.add(s[R])
                R += 1
            maxLen = max(maxLen, R - L)
            while (R < N and s[R] in appear):
                appear.remove(s[L])
                L += 1
        return maxLen
                
                