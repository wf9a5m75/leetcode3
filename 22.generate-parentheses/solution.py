from typing import List, Dict

class Solution:
    def __init__(self):
        self.parenthesis_cache: Dict[int, str] = {}
        
    def generateParenthesis(self, n: int) -> List[str]:
        if (n == 0):
            return [""]
        
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