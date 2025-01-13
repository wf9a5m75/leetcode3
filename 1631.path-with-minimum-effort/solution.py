#
# M ... heights.length
# N ... heights[0].length
#
# Time complexity: O(M x N)
# Space complexity: O(M x N)
#
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        INF = float('inf')
        rows = len(heights)
        cols = len(heights[0])
        if (rows == 1 and cols == 1):
            return 0
        
        dp = [[INF] * cols for _ in range(rows)]
        dp[0][0] = 0

        q=[(0,0)]
        while q:
            y, x = q.pop(0)
            for dy, dx in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                if (x + dx < 0 or x + dx == cols or y + dy < 0 or y + dy == rows):
                    continue
                
                difference = max(dp[y][x], abs(heights[y][x] - heights[y + dy][x + dx]))
                if (difference < dp[y+dy][x+dx]):
                    dp[y+dy][x+dx] = difference
                    q.append((y+dy, x+dx))
        return dp[rows-1][cols-1]
