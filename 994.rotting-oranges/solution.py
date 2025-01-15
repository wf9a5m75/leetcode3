from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        freshOranges = 0
        q = deque()
        for y in range(rows):
            for x in range(cols):
                if grid[y][x] == 2:
                    q.append([y, x])
                elif grid[y][x] == 1:
                    freshOranges += 1

        minutes = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q and freshOranges > 0:
            nextQ = deque()
            while q and freshOranges > 0:
                y, x = q.popleft()
                if grid[y][x] == 1:
                    grid[y][x] = 2
                    freshOranges -= 1
                for dy, dx in directions:
                    nextY = y + dy
                    nextX = x + dx
                    if nextY < 0 or nextY == rows or nextX < 0 or nextX == cols:
                        continue
                    if grid[nextY][nextX] != 1:
                        continue
                    nextQ.append([nextY, nextX])
            q = nextQ
            if q and freshOranges > 0:
                minutes += 1
        if freshOranges > 0:
            return -1
        return minutes
