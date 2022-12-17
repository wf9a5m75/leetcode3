class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        actions = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(x / y)
        }
        stack = []

        for t in tokens:
            if (not stack):
                stack.append(t)
                continue

            if (t not in actions):
                stack.append(t)
                continue

            val2 = int(stack.pop())
            val1 = int(stack.pop())
            value = actions[t](val1, val2)
            # print(val1, t, val2, "->", value)
            stack.append(str(value))

        result = 0
        for t in stack:
            result += int(t)
        return result
