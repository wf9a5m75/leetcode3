class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        result = 0
        open_cnt = 0
        for char in s:
            
            if open_cnt == 0 and char == ")":
                # We need a "("
                result += 1
                continue
            
            if char == "(":
                open_cnt += 1
            else:
                open_cnt -= 1
        
        # If some open parenthesis are remained,
        # we need to insert the closer parenthesis somewhere.
        result += open_cnt
        
        return result