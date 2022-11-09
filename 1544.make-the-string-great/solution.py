class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for char in s:
            isLower = char.islower()
            lwChar = char.lower()
            upChar = char.upper()

            if (stack):
                lastIsUpper = stack[-1].isupper()
                if ((isLower and lastIsUpper and upChar == stack[-1]) or
                   (not isLower and not lastIsUpper and lwChar == stack[-1])):
                    stack.pop()
                    continue
            stack.append(char)

        return "".join(stack)
