class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maxLength = 0
        substring = set()
        for right, char in enumerate(s):
            char = s[right]
            if char in substring:
                maxLength = max(maxLength, right - left)
                while left < right and s[right] in substring:
                    substring.remove(s[left])
                    left += 1
            substring.add(char)

        maxLength = max(maxLength, len(s) - left)
        return maxLength
