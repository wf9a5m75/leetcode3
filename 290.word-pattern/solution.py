class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        keys = {}
        values = {}
        words = s.split(" ")
        if (len(words) != len(pattern)):
            return False
        for i, pChar in enumerate(pattern):
            word = words[i]
            if word in values:
                if (values[word] != pChar):
                    return False
            elif pChar in keys:
                if (keys[pChar] != word):
                    return False
            else:
                keys[pChar] = word
                values[word] = pChar
        return True
