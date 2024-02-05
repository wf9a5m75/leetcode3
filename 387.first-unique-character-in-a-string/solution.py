class Solution:
    def firstUniqChar(self, s: str) -> int:
        memo = defaultdict(int)
        for char in s:
            memo[char] += 1
        
        for i in range(len(s)):
            char = s[i]
            if (memo[char] == 1):
                return i
        return -1