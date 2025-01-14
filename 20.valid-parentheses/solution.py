class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            "[": "]",
            "(": ")",
            "{": "}"
        }

        stack = []
        for char in s:
            if char in pairs:
                stack.append(pairs[char])
                continue
            if stack and stack[-1] == char:
                stack.pop()
                continue
            return False
        return len(stack) == 0
