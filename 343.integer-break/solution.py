class Solution:
    def integerBreak(self, n: int) -> int:
        if (n == 2):
            # 2 = 1 + 1, result = 1 * 1
            return 1
        if (n == 3):
            # 3 = 2 + 1, result = 2 * 1
            return 2
        
        @cache
        def backtrack(n):
            if (n >= 0 and n <= 1):
                return 1
            
            result = 0
            if (n - 3 >= 0):
                result = 3 * backtrack(n - 3)

            result = max(result, 2 * backtrack(n - 2))
            return result
        return backtrack(n)