class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = set()
        result = 0
        left = 0
        for right, char in enumerate(list(s)):

            while (char in substr):
                substr.remove(s[left])
                left += 1
            result = max(result, right - left + 1)
            substr.add(char)
        return result
