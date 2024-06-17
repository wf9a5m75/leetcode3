from typing import Dict, List

class Solution:
    def __init__(self):
        self.parenthesis_cache: Dict[int, str] = {}

    def generateParenthesis(self, n: int) -> List[str]:
        """
        Logic:
            n = 0   [""]    This is the seed
            n = 1  
                ("") + "" -> ["(A)"]
            n = 2
               ("") + (A) -> ["(C)(A)"]
               ((A)) + "" -> ["((B))"]
            n = 3
                ("") + (C)(A) -> ["()()()"]
                ("") + ((B)) -> ["()(())"]
                
                ((A)) + (A) -> ["(())()"]
                
                (((B))) + "" -> ["((()))"]
                ((C)(A)) + "" -> ["(()())"]
                
        """
        if (n == 0):
            return [""]  # seed
        
        if (n in self.parenthesis_cache):
            return self.parenthesis_cache[n]
        
        results: List[str] = []
        
        for left_count in range(n):
            for left_hand in self.generateParenthesis(left_count):
                
                right_count = n - 1 - left_count
                for right_hand in self.generateParenthesis(right_count):
                    results.append(f"({left_hand})" + right_hand)
        
        self.parenthesis_cache[n] = results
        return results