#
# M ... heights.length
# N ... heights[0].length
#
# The following code is essentially performing a Dijkstra-like search on a 2D grid.
# Each cell in the grid is treated as a node in a graph,
# and the "cost" (or weight) of moving between two adjacent cells is
# based on the absolute difference in their heights.
#
# - Nodes(Vertices): Each cell in the gris, so V = rows x cols
#
# - Edges: From each cell, we can move up to 4 directions (up, down, left, right).
#          Thus, in total, the graph can have about 4 x V edges.
#          (in reality, boundary cells have fewer than 4 neighbors, but asymptotically it's the same.)
#
# [Dijkstra's Algorithm Complexity]
# Dijkstra's algrothm (when implemented with a priority queue, like a binary heap) has following complexity:
#   O(E log V)
#
# where
#   - E is the number of edges,
#   - V is the number of vertices (nodes).
#
# In this problem case,
#   - V = rows x cols = MN
#   - E ≈ 4V
# Thus,
#   O(E log V)≈O((4V)log V) = O(V log V)
# Substituting V = rows x cols
#   O((M x N) log (M x N))
# -----------------------------------------------------------------------
# Time complexity: O((M x N) log (M x N))
# Space complexity: O(M x N)
#
from heapq import heappush,heappop

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        INF = float('inf')
        rows = len(heights)
        cols = len(heights[0])
        if (rows == 1 and cols == 1):
            return 0
        
        dp = [[INF] * cols for _ in range(rows)]
        dp[0][0] = 0

        q=[(0,0,0)] # effort, y, x
        while q:
            effort, y, x = heappop(q)
            for dy, dx in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                if (x + dx < 0 or x + dx == cols or y + dy < 0 or y + dy == rows):
                    continue
                
                difference = max(dp[y][x], abs(heights[y][x] - heights[y + dy][x + dx]))
                if (difference >= dp[y+dy][x+dx]):
                    continue
                
                dp[y+dy][x+dx] = difference
                heappush(q, (difference, y+dy, x+dx))

        return dp[rows-1][cols-1]
