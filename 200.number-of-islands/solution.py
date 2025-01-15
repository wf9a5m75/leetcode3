from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        islands = 0
        for y in range(rows):
            for x in range(cols):
                if grid[y][x] != "1":
                    continue
                self.fillIsland(grid, y, x)
                islands += 1

        for y in range(rows):
            for x in range(cols):
                if grid[y][x] == "-1":
                    grid[y][x] = "1"
        return islands
    
    def fillIsland(self, grid: List[List[int]], startY: int, startX: int) -> None:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        q.append((startY, startX))
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        while q:
            y, x = q.popleft()
            if grid[y][x] != "1":
                continue
            grid[y][x] = "-1"
            for dy, dx in directions:
                nextX = max(0, min(cols - 1, x + dx))
                nextY = max(0, min(rows - 1, y + dy))
                q.append((nextY, nextX))
