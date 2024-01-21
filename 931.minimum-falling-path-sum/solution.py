class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        MAX_INT = 2**31 - 1
        dp = [[0] * n for _ in range(2)]
        
        curIdx = 0
        nextIdx = 1
        for y in range(n):
            for x in range(n):
                dp[nextIdx][x] = MAX_INT
                
            for x in range(n):
                if (x > 0):
                    dp[nextIdx][x - 1] = min(
                        dp[nextIdx][x - 1],
                        dp[curIdx][x] + matrix[y][x]
                    )
                
                dp[nextIdx][x] = min(
                    dp[nextIdx][x],
                    dp[curIdx][x] + matrix[y][x]
                )
                if (x + 1 < n):
                    dp[nextIdx][x + 1] = min(
                        dp[nextIdx][x + 1],
                        dp[curIdx][x] + matrix[y][x]
                    )
            curIdx, nextIdx = nextIdx, curIdx
        return min(dp[curIdx])