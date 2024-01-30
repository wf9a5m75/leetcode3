from typing import List

class Solution:
    def __init__(self):
        self.operators = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b),
        }
        
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        while(tokens):
            
            token = tokens.pop(0)
            if (token in self.operators):
                rhv = stack.pop()
                lhv = stack.pop()
                result = self.operators[token](lhv, rhv)
                stack.append(result)
            else:
                stack.append(int(token))
        
        return stack.pop()