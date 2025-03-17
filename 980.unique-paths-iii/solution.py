class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        start = 1
        goal = 2
        can_move = 0
        block = -1
        visited = -2

        m = len(grid)
        n = len(grid[0])

        # find the start position
        start_pos = [inf, inf]
        goal_pos = [inf, inf]
        empty_cells = 0
        for y in range(m):
            for x in range(n):
                if grid[y][x] == start:
                    start_pos = [y, x]
                    empty_cells += 1
                elif grid[y][x] == can_move:
                    empty_cells += 1
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def backtrack(y: int, x: int) -> int:
            nonlocal empty_cells
            
            if grid[y][x] == visited or grid[y][x] == block:
                return 0
            if grid[y][x] == goal and empty_cells == 0:
                return 1
            
            empty_cells -= 1
            org_value = grid[y][x]
            grid[y][x] = visited
            result = 0
            for dy, dx in directions:
                next_y = max(min(m - 1, dy + y), 0)
                next_x = max(min(n - 1, dx + x), 0)
                result += backtrack(next_y, next_x)
            grid[y][x] = org_value
            empty_cells += 1
            return result
        
        return backtrack(start_pos[0], start_pos[1])
