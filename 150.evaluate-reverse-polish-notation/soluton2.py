class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        calculations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b)
        }
        while len(tokens) > 2:
            while len(tokens) > 3 and (
                tokens[-2] in calculations or tokens[-3] in calculations
            ):
                stack.append(tokens.pop())
            
            action = tokens.pop()
            b = int(tokens.pop())
            a = int(tokens.pop())
            result = calculations[action](a, b)
            tokens.append(f"{result}")
            while stack and not(tokens[-1] in calculations):
                tokens.append(stack.pop())
        return int(tokens[0])
