class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = [""]
        for c in s:
            if (stack[-1] == c):
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)
