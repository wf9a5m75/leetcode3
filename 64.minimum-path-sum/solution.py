class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        INF = float('inf')
        dp = [[INF] * (N + 1) for _ in range(M + 1)]
        dp[0][0] = grid[0][0]

        for y in range(M):
            for x in range(N):
                dp[y + 1][x] = min(dp[y + 1][x], dp[y][x] + grid[y][x])
                dp[y][x + 1] = min(dp[y][x + 1], dp[y][x] + grid[y][x])
        return dp[M - 1][N - 1]
