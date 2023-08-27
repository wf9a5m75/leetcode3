class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lenHaystack = len(haystack)
        lenNeedle = len(needle)
        
        for i in range(lenHaystack - lenNeedle + 1):
            
            L = 0
            R = lenNeedle - 1
            while ((L <= R) and
                   (haystack[i + L] == needle[L]) and 
                   (haystack[i + R] == needle[R])):
                L += 1
                R -= 1
            if (L > R):
                return i
        return -1