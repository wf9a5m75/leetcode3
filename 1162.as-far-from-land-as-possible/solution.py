class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        INF = 100000
        N = len(grid)
        dp = [[INF] * N for _ in range(N)]

        for y in range(N):
            for x in range(N):
                if (grid[y][x] == 1):
                    dp[y][x] = 0
                else:
                    fromUpper = dp[y - 1][x] + 1 if y - 1 >= 0 else INF
                    fromLeft = dp[y][x - 1] + 1 if x - 1 >= 0 else INF
                    dp[y][x] = min(dp[y][x], fromUpper, fromLeft)

        result = -1
        for y in range(N - 1, -1, -1):
            for x in range(N - 1, -1, -1):
                if (grid[y][x] == 1):
                    dp[y][x] = 0
                else:
                    fromBottom = dp[y + 1][x] + 1 if y + 1 < N else INF
                    fromRight = dp[y][x + 1] + 1 if x + 1 < N else INF
                    dp[y][x] = min(dp[y][x], fromBottom, fromRight)
                    result = max(result, dp[y][x])
        if (result == INF):
            result = -1
        return result
